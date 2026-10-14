# Lab 5 Submission — Static Code Analysis

## Deliverables
- `course_enrollment_system.py` — cleaned course enrollment program.
- `issues.md` — issues found in the original GitHub source and their fixes. Line numbers refer to the original file.
- `reflection.md` — reflection responses. The provided handout describes the reflection deliverable but does not include the exact four questions, so the answers use standard reflection prompts; replace them if your instructor gave exact wording elsewhere.

## Run the program
Use Python 3.10 or newer (the script uses built-in generic type annotations).

```bash
python course_enrollment_system.py
```

## Install and run static analysis

```bash
python -m pip install pylint bandit flake8
pylint course_enrollment_system.py > pylint_report.txt
bandit -r course_enrollment_system.py > bandit_report.txt
flake8 course_enrollment_system.py > flake8_report.txt
```

Open the three report files and check the output. Tool reports are intentionally not supplied as if they had been run: Pylint, Bandit, and Flake8 were not installed in the preparation environment. Include the actual reports/score after running them locally.

## Important behavior changes
- Scholarship calculation now takes a numeric discount rate (e.g. `0.25` for 25%) instead of a Python expression string.
- The demo no longer prints a hard-coded registrar token.
- The roster is written without invoking a shell command.
