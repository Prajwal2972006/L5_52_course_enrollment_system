# Static Analysis Issues — Course Enrollment System

**Target:** `course_enrollment_system.py`  
**Line-number note:** The line numbers below refer to the original GitHub file `course_enrollment_system.py` (87 lines), before fixes. The tool reports must be generated locally after installing Pylint, Bandit, and Flake8; they are not fabricated here.

| Issue | Type / Severity | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Arbitrary expression execution with `eval()` | Security — High | 44–47 | `calculateScholarshipTuition()` evaluates a caller-provided string, which can execute arbitrary Python code. | Removed `eval()`. Accept a numeric discount rate and validate it is between `0.0` and `1.0`. |
| Hard-coded registrar secret printed to output | Security — High | 74, 83 | A token-like secret is embedded in the source and printed, exposing a credential. | Removed the literal secret and stopped printing credentials. A real application should load secrets from secure configuration. |
| Shell command built from filename | Security — Medium | 58–62 | `os.system()` runs a shell command containing the filename, creating command-injection risk. | Removed shell execution; use `pathlib.Path` for file output and print a normal status message. |
| Insecure random OTP generation | Security — Medium | 54–55 | `random.randint()` is not designed for security-sensitive token generation. | Use `secrets.randbelow()` to generate a four-digit OTP. |
| Mutable default argument | Correctness / Maintainability — Medium | 14 | `audit_trail=[]` is shared between function calls, so entries can leak across enrollments. | Use `None` as the default and initialize a new list within the function. |
| Bare exception silently swallowed | Reliability — Medium | 26–31 | Bare `except:` catches all exceptions and `pass` hides failures. | Use a dictionary lookup and return `False` for an unknown course instead of silently swallowing errors. |
| Enrollment can create inconsistent seat state | Correctness — Medium | 16–20 | Enrollment checks the course's closed flag but does not independently validate that seats remain available. | Validate course existence, closed status, and available seats; mark the course closed when seats reach zero. |
| Unknown course / unrestricted discount expression | Correctness / Security — Medium | 44–47 | Unknown course IDs can raise `KeyError`, and the discount expression is unrestricted. | Validate course existence and discount-rate bounds before calculating tuition. |
| Weak hash algorithm | Security — Low/Medium | 50–51 | MD5 is outdated for security-sensitive uses. | Replaced MD5 with SHA-256. A plain hash should not be used for password storage. |
| File handle manually managed | Reliability / Style — Low | 58–61 | Manual `open()` and `close()` can leave the file open if an exception occurs. | Use `Path.write_text()` with an explicit encoding. |
| Naming, formatting, and missing documentation | Style / Maintainability — Low | Throughout | CamelCase function names and old `%` formatting reduce consistency and readability. | Use `snake_case`, f-strings, docstrings, and consistent formatting. |
| Unused import and variable | Code quality — Low | 3, 35 | `math` and `lab_fee` are unused. | Removed the unused import and variable. |

## Verification status

The cleaned script has been syntax-checked and functionally exercised in the preparation environment. Pylint, Bandit, and Flake8 were not installed in that environment, so no genuine tool reports or final Pylint score are claimed. Run the commands in `README_SUBMISSION.md` on your computer and include the generated reports if your instructor requests them.
