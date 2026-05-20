#!/usr/bin/env python3
"""Generate a single image with Gemini's image-preview models. Reads GEMINI_API_KEY from .env."""
import base64
import json
import os
import sys
from pathlib import Path

import requests


def load_env():
    for p in [Path(__file__).resolve().parent.parent / ".env",
              Path.cwd() / ".env"]:
        if p.exists():
            for line in p.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
            return


def main():
    if len(sys.argv) < 3:
        print("usage: gen_image.py <prompt_file> <output_png> [model]", file=sys.stderr)
        sys.exit(2)
    prompt_file, out = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "gemini-3-pro-image-preview"

    load_env()
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("missing GEMINI_API_KEY in .env", file=sys.stderr)
        sys.exit(1)

    prompt = Path(prompt_file).read_text()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    r = requests.post(url, json=payload, timeout=180)
    if r.status_code != 200:
        print(f"API error {r.status_code}: {r.text[:500]}", file=sys.stderr)
        sys.exit(1)

    data = r.json()
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                Path(out).write_bytes(base64.b64decode(inline["data"]))
                print(f"wrote {out} ({Path(out).stat().st_size} bytes)")
                return
    print(f"no image in response: {json.dumps(data)[:500]}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
