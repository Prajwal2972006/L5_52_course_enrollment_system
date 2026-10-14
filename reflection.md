# Reflection — Static Code Analysis

> **Question wording note:** The uploaded lab handout explains the reflection deliverable but does not show the four reflection questions. The answers below use four standard reflection prompts. If your instructor provided exact questions separately, replace these prompts with that wording.

## 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without running the program. Pylint focuses on code quality and likely programming mistakes, Flake8 checks style and common errors, and Bandit looks for insecure coding patterns. Using all three gives broader coverage than relying on manual review alone.

## 2. What issues did you find, and which were most important?

The most serious issue was `eval()` on a supplied expression because it could execute arbitrary Python code. A hard-coded token was also exposed in the source and printed. Other issues included a shell command constructed from a filename, a predictable OTP generator, a mutable default list, and a broad exception handler that silently ignored failures. I prioritized security and correctness before style improvements.

## 3. How did you fix the issues, and how did you verify the changes?

I replaced expression evaluation with a validated numeric discount rate, removed shell execution, switched OTP generation to `secrets`, changed the mutable default to `None`, removed the bare exception handler, and added course/seat validation. I also improved naming, documentation, file writing, and hashing. Verification should include running the program, exercising valid and invalid inputs, and rerunning Pylint, Bandit, and Flake8 to confirm that the addressed findings disappear. Record the actual local tool output before submission; do not claim a score or a clean report without running the tools.

## 4. What are the limitations of static analysis, and what did you learn?

Static analysis can flag suspicious patterns, but it cannot prove that the program behaves correctly in every situation. It may miss business-logic bugs or report issues that require human judgment. Testing and code review are still necessary. I learned that small coding choices—such as `eval()`, mutable defaults, and broad exception handling—can create meaningful security and reliability risks.
