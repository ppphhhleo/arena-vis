```markdown
# vis-arena Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and practices used in the `vis-arena` Python codebase. You'll learn about the project's file naming conventions, import/export styles, commit patterns, and how to write and run tests. These guidelines help ensure consistency and maintainability across the repository.

## Coding Conventions

### File Naming
- Use **kebab-case** for file names.
  - Example:  
    ```
    data-processor.py
    visualization-utils.py
    ```

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .data-processor import DataProcessor
    from .visualization-utils import render_chart
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    __all__ = ['DataProcessor', 'render_chart']
    ```

### Commit Patterns
- Commit messages are **freeform** (not strictly conventional).
- Commonly use prefixes, but not enforced.
- Average commit message length: ~80 characters.

## Workflows

### Adding a New Module
**Trigger:** When you need to add new functionality as a separate module  
**Command:** `/add-module`

1. Create a new Python file using kebab-case (e.g., `my-new-module.py`).
2. Implement your logic using relative imports for any internal dependencies.
3. Define `__all__` in the module to specify named exports.
4. Add or update tests in a corresponding `*.test.*` file.

### Running Tests
**Trigger:** When you want to verify code correctness  
**Command:** `/run-tests`

1. Locate test files matching the pattern `*.test.*`.
2. Use the project's preferred test runner (framework not specified; check for `pytest` or similar).
3. Run the tests and review output for failures.

### Refactoring Imports
**Trigger:** When reorganizing code or moving files  
**Command:** `/refactor-imports`

1. Update import statements to use relative paths.
2. Ensure all references are updated in dependent modules.
3. Run tests to confirm nothing is broken.

## Testing Patterns

- Test files follow the pattern: `*.test.*` (e.g., `data-processor.test.py`).
- The specific testing framework is unknown; check for `pytest`, `unittest`, or similar.
- Place tests alongside the code they test or in a dedicated test directory.
- Example test file:
  ```python
  # data-processor.test.py
  from .data-processor import DataProcessor

  def test_process_data():
      dp = DataProcessor()
      assert dp.process([1, 2, 3]) == [2, 3, 4]
  ```

## Commands
| Command         | Purpose                                 |
|-----------------|-----------------------------------------|
| /add-module     | Scaffold a new module with conventions  |
| /run-tests      | Run all test files in the repository    |
| /refactor-imports | Update imports to match new structure |
```
