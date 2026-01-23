```instructions
# Copilot / AI agent instructions for this repository

This repository contains small Python competitive-programming style solutions and helper utilities. Use the guidance below to make targeted, low-risk edits and produce idiomatic outputs.

1. Project overview
- Small, single-file Python solutions (entrypoints) live at the repo root (for example [watermelon.py](watermelon.py) and [lab1.py](lab1.py)).
- Typical pattern: read from standard input using `input()` or `sys.stdin`, compute, print a single result. Expect code to be used in contest-style runs rather than as a library.

2. Important conventions and patterns
- Do not introduce heavy dependencies: the project is intended to run with the Python standard library only.
- Prefer minimal changes: edits normally fix algorithmic logic, I/O format, or remove interactive prompts.
- Many files currently include human prompts in `input()` calls (e.g. `input("Enter a number : ")`). Remove prompts when making automated/scripted changes so input is raw (e.g. `int(input())`).
- Keep functions small and deterministic. If adding helpers, place them in the same file unless adding a true shared module.

3. Python version and typing
- Repository uses modern typing hints (e.g. `list[int]`). Assume Python 3.9+ when suggesting syntax or typing changes.

4. Build / run / debug
- No build system or tests are present. To run a script locally:

  python3 watermelon.py

- For multi-input or sample testing, prefer piping files or heredocs instead of adding prompts.

5. Code edits the agent should make autonomously
- Fix obvious logic bugs, off-by-one errors, and inefficient loops (replace O(n^2) where a trivial O(n sqrt n) is appropriate).
- Normalize I/O: remove `input` prompts, avoid prints other than required output, and keep output formatting exact.
- When adding examples or doctests, keep them minimal and inline in the same file.

6. What to avoid
- Don't add frameworks, CI, or packaging changes without explicit user approval.
- Don't rename top-level script files or move many files into new modules without the user's OK.

7. Examples from this repo
- `lab1.py` currently reads a single integer and prints `Yes`/`No`. When editing, remove the input prompt string and ensure output matches expected judge format.
- `watermelon.py` is a compact algorithmic helper set — keep helper functions inside the file and avoid global side effects. If converting to testable functions, add a small `main()` and keep CLI behavior consistent.

8. Teaching / Language-level (CRITICAL)
- Big rule (EMPHASIZE): Assume the user is a pre-intermediate English speaker preparing for ICPC in "learning mode." When the user requests explanations or asks questions, DO NOT respond with code-only answers.
- Instead: explain concepts in very simple English, use short sentences, step-by-step breakdowns, and concrete examples. Use minimal jargon. Prefer analogies and numbered steps.
- When a code change is necessary, first provide a plain-English explanation of *why* the change is needed and *what* it does. Offer the code only after the user explicitly asks for it, or include a clearly marked optional code block at the end.
- Examples:
  - If the user asks why `lab1.py` fails on edge cases, explain the logic error in plain terms and list a short checklist to fix it. Only offer a patched snippet if they request it.
  - If teaching how to remove `input()` prompts, show the before/after in one-line pseudo-steps and keep the final code optional.
- Ask quick comprehension checks (1-2 simple questions) after explanations, and offer a short practice suggestion (small input to try or a variant problem).

If anything here is incorrect or you want more detail about running or refactoring, tell me which area to expand.

```

9. Testing / Creating test files
- When a user asks you to "create a test file" for a Python script, always produce a runnable, robust test under a `tests/` folder that uses the standard library only.
- Preferred approach: create a `tests/test_<scriptname>.py` that uses `unittest` and runs the target script as a subprocess. This works well for contest-style scripts that read from `input()`.
- Requirements for test files you generate:
  - Use `sys.executable` to invoke the same Python interpreter.
  - Use `subprocess.run(..., input=..., text=True, capture_output=True)` to feed stdin and capture stdout/stderr.
  - Normalize outputs with `.strip()` before asserting to tolerate trailing newlines/whitespace.
  - Include a small helper `run_script(path, input_str)` and multiple test cases in a `unittest.TestCase`.
  - Do not modify the user's source files; tests should exercise the file as-is unless the user explicitly asks for a source change.
  - Keep the tests dependency-free so they run with `python -m unittest discover -v`.

Example test (for `lab1.py`):

```python
import sys
import subprocess
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / 'lab1.py'

def run_script(path, input_str):
  proc = subprocess.run([sys.executable, str(path)], input=input_str, text=True, capture_output=True)
  return proc.stdout.strip()

class Lab1Tests(unittest.TestCase):
  def test_even_two(self):
    out = run_script(SCRIPT, '2\n')
    self.assertEqual(out, 'No')

  def test_even_four(self):
    out = run_script(SCRIPT, '4\n')
    self.assertEqual(out, 'Yes')

if __name__ == '__main__':
  unittest.main()
```

Run tests with:

```bash
python -m unittest discover -v
```

When you finish creating the test file, mention any assumptions made about inputs and any places the test might fail due to interactive prompts in the source.
