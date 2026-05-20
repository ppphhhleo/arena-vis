# Flyer Print Notes

Quick reference for sending VISxGenAI 2026 flyers to print. Updated 2026-05-19.

## Flyer roster

There are now **12 flyers + 1 review gallery**, all sized at **A4 trim (210 × 297 mm)** with `@page { size: A4; margin: 0 }`. Critical content (text, QRs, organizers) sits inside a safe zone of **14 mm** from each edge (12–13 mm on Bold Mono and Bold Poster).

| # | File | Style | Hero band | Print risk |
|---|---|---|---|---|
| 01 | `editorial-tri-tone.html` | Burgundy / pink / cream tri-band | **Burgundy `#7A1F35`** (heavy) | High — paper warp on inkjet |
| 02 | `dd-editorial.html` | DD-brown / peach / cream three-band | **Brown `#653819`** (heavy) | High — paper warp on inkjet |
| 03 | `soft-editorial.html` | Pastel cream paper | Cream `#F2EEDF` | Low |
| 04 | `warm-editorial.html` | Warm-pastel paper | Cream `#F2EEDF` | Low |
| 05 | `bold-poster.html` | Off-white poster | Near-white | **Lowest** |
| 06 | `bold-mono.html` | Cream + DD palette | Cream | Low |
| 08 | `soft-systems.html` | Gradient pastel | Light pastel gradient | Low |
| 09 | `future-nostalgia.html` | Gradient pastel | Light pastel gradient | Low |
| 10 | `engraving.html` | Vintage engraving CFP | Cream paper with framed inset | Low–medium (cream illustration uses some coverage) |
| 11 | `editorial-tri-tone-light.html` | **Print-light variant of 01** | Off-white `#FFFAF2` | **Lowest** |
| 12 | `dd-editorial-light.html` | **Print-light variant of 02** | Cream `#FFF8F0` | **Lowest** |

The two `-light` variants drop the heavy dark hero band (saving ~60–70 % of ink coverage vs. their parents) while keeping all typography, accent colors, and the IEEE VIS 2026 logo in place. Use these for home / office printing; use the originals if you're sending to a copy shop and want the bolder look.

## Trim & bleed

**For pro print with bleed:**
- Export to PDF, open in a vector editor (Illustrator / Affinity), and place on a 216 × 303 mm canvas with 3 mm bleed on each side.
- Extend any full-bleed color blocks (the burgundy / pink / cream bands in 01, the brown / peach bands in 02) past the 210 × 297 mm trim line by 3 mm so trim drift doesn't expose paper.
- Add crop marks.

**For home / office print:**
- Print at 100 % scale, "actual size", no shrink-to-fit.
- **#05 Bold Poster** and the **#11 / #12 light variants** are the safest picks.
- Avoid #01 Editorial Tri-Tone and #02 DD Editorial on inkjet — the dark bands will warp paper and stripe.

## Color management — RGB → CMYK

The flyers are authored in sRGB. CMYK conversion will shift several colors. None of these are deal-breakers, but know what to expect.

| Flyer | Color | Hex | CMYK behavior | Pantone equivalent |
|---|---|---|---|---|
| 01 Editorial Tri-Tone | Burgundy | `#7A1F35` | Slightly muddier red-brown; cross-hatching in shadow areas | **PMS 188 C** |
| 02 DD Editorial | DD Brown | `#653819` | Reproduces faithfully | **PMS 1545 C** (Dunkin's actual brand) |
| 02 DD Editorial | DD Orange | `#FF671F` | Loses noticeable saturation — no full-strength CMYK orange | **PMS 165 C** (Dunkin's brand) |
| 02 DD Editorial | DD Magenta | `#DA1884` | Loses some punch but stays recognizably magenta | **PMS 219 C** (Dunkin's brand) |
| 05 Bold Poster | Red | `#D8000F` | Drops slightly to muddy orange-red | **PMS 185 C** |
| 10 Engraving | Coral accent | `#D9532A` | Reproduces well in CMYK | **PMS 173 C** |

If brand color accuracy matters (especially for the DD palette in #02 / #06), ask the print shop to use Pantone spot inks for those swatches instead of CMYK process build.

The pastels in #03 Soft Editorial, #04 Warm Editorial, #08 Soft Systems, and #09 Future Nostalgia all sit comfortably in the CMYK gamut and will reproduce well as process color.

## Recommended printer choice per flyer

| Flyer | Home inkjet | Office laser | Copy shop / pro |
|---|---|---|---|
| 01 Editorial Tri-Tone | **Avoid** (paper warp) | OK (toner streak risk) | **Best** |
| 02 DD Editorial | **Avoid** (paper warp) | OK (toner streak risk) | **Best** (for DD Pantone match) |
| 03 Soft Editorial | OK | Best | Best |
| 04 Warm Editorial | OK | Best | Best |
| 05 Bold Poster | **Best** — white bg | Best | Best |
| 06 Bold Mono | OK | OK | **Best** (for DD Pantone match) |
| 08 Soft Systems | OK | OK | Best |
| 09 Future Nostalgia | OK | OK | Best |
| 10 Engraving | OK (low coverage) | Best | **Best** for the fine engraving detail |
| 11 Tri-Tone Light | **Best** — replaces 01 for inkjet | Best | OK (use 01 for richer pro print) |
| 12 DD Editorial Light | **Best** — replaces 02 for inkjet | Best | OK (use 02 for richer pro print) |

## Typography references (since 2026-05-19 redesign)

- **Title face**: Instrument Serif (01, 02, 09, 11, 12), Cormorant Garamond (03, 04), Libre Baskerville (05, 06), Playfair Display (10), Outfit / Bricolage Grotesque elsewhere
- **Deadline date face**: `DM Serif Display` 22pt — applied uniformly across flyers 01–06, 08, 09, 11, 12. Each flyer renders the date in its own native accent color (burgundy / ink / red / orange / magenta) for brand consistency.
- **Deadline label face**: Bricolage Grotesque 500 13pt or each flyer's native sans, label sits **above** the date.
- **IEEE VIS 2026 logo placement**: Inline in the header next to the date / venue line, **50 mm wide**, no backdrop. The logo's brown letterforms have low contrast on the dark hero bands of 01 / 02 — that's why the light variants 11 / 12 exist.

## QR codes

Both QRs (`qr.png` Website + `discord-qr.png` Discord) are placed at **25 × 25 mm** with built-in white quiet zone. This is at the lower edge of reliable scan size — if you have room to bump them to 28–30 mm, do it. Don't shrink below 25 mm.

The website QR label now reads as a **URL** (`visxgenai.github.io`, Bricolage Grotesque 500 7.5pt, lowercase) instead of just the word "Website", so even non-scanners can read the destination.

Test-scan both with two different phones before sending to print.

## Other notes

- **Affiliations under organizer names are 9–9.5 pt.** Readable held in hand or up close on a poster board, but not from across a hallway. If the flyer will be wall-posted at >2 m, consider dropping affiliations and just listing organizer names.
- **The sponsor slot is currently a placeholder** (`<div class="sp-slot">sponsor logo</div>`). Drop in the real logo before print:
  ```html
  <div class="sp-slot"><img src="sponsor.png" style="max-width:100%;max-height:100%;object-fit:contain;"></div>
  ```
- **Discord QR currently encodes** `https://discord.gg/visxgenai` as a placeholder. Regenerate `discord-qr.png` once the real invite URL exists:
  ```bash
  python3 -c "import qrcode; qrcode.make('YOUR_REAL_DISCORD_URL').save('flyer/discord-qr.png')"
  ```
- **IEEE VIS 2026 logo** is the official SVG from <https://ieeevis.org/year/2026/assets/vis2026_logo.svg> (saved as `flyer/vis2026_logo.svg`). The logo's brown letterforms have low contrast on the dark hero bands of #01 / #02 — use the `-light` variants for home print or add a cream backdrop pad before pro print if keeping the dark variant.

## Recent fixes & changes

### 2026-05-19

- **#11 and #12 added** — print-light variants of Editorial Tri-Tone and DD Editorial. Dark hero bands replaced with cream backgrounds; typography preserved.
- **Logo placement** moved from corner-floating to inline beside the date/venue line in every flyer's header, sized at 50 mm wide.
- **Deadline timeline** restyled across all flyers: labels above (sans 13pt), dates below in **DM Serif Display 22pt** in each flyer's accent color.
- **Website QR label** changed from "Website" to the actual URL `visxgenai.github.io` for added scannability.
- **"Tracks · 01 / 02" meta tag** removed from the middle-section headers on #01, #02, #09 to declutter.

### 2026-05-06

- Bumped 0.5 px hairline borders to 1 px on Editorial Tri-Tone footer divider and across Soft Editorial (masthead, deadlines, org-section, QR, sponsor slot) — anything below ~0.75 pt risks disappearing on cheaper print stock.
- Raised the Track I / Track II divider rule on Soft Editorial from 0.4 to 0.6 opacity so the line stays visible after dot gain.
