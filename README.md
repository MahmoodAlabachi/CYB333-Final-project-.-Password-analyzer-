# Password Strength Analyzer

**Security Automation Project | Python command-line program**

## Project overview

This project automates **basic, rule-based evaluation of fictional sample passwords**. It compares each sample with an intentionally small list of common passwords; checks minimum length and character types; detects runs of repeated characters; finds simple ascending, descending, and keyboard sequences; and explains an estimated Weak, Medium, or Strong rating. It is a **learning demonstration**, not a production password verifier or a guarantee of security.

The tool runs locally in a terminal. The program contains **no network or file-writing code for entered passwords**. For safe use, **never test a real account password**. The built-in demonstration uses invented examples only.

## Features

- Checks for 8+ characters, with an extra point for 12+ characters.
- Checks for uppercase and lowercase letters, numbers, and symbols.
- Compares whole entries against a **20-entry local common-password list** (case-insensitive).
- Flags three repeated adjacent characters (case-insensitive).
- Flags three consecutive characters from alphabet, numeric, or selected keyboard runs, including ascending and descending order.
- Displays all detected issues and improvement suggestions at once.
- Offers an interactive command-line interface, a built-in demo, and repeatable unit tests.
- Uses Python's `getpass()` when possible, so entered text is not echoed in a compatible terminal.

## Prerequisites and dependencies

- Python **3.8 or newer** (recommended Python 3.10+).
- Windows, macOS, or Linux terminal.
- **No external packages**. Python standard-library modules: `argparse`, `getpass`, `unittest`.
- No internet connection, API key, database, account, or separate dataset needed.

## Folder structure

```text
Password_Strength_Analyzer_Project/
├── password_analyzer.py             # Main program, documented functions
├── test_password_analyzer.py        # Automated unit tests
├── README.md                        # This setup and usage guide
├── CODE_REVIEW.md                   # Findings and explanation of code updates
├── Final_Project_Report.docx        # Written final report
└── 
    ├── demo_output.txt              # Captured output of a real demo run
    ├── test_results.txt             # Captured output of 18 unit tests
    ├── demo_weak_output.png         # Captured weak/common result excerpt
    ├── demo_medium_strong_output.png # Captured Medium/Strong results
    └── test_results.png             # Captured unit-test summary
```

## Setup and running the program

1. Download/unzip the project and open a terminal in the folder containing `password_analyzer.py`.
2. Verify Python: `python --version` (on some computers, use `python3 --version`, or Windows `py --version`).
3. Run the interactive analyzer:

   ```bash
   python password_analyzer.py
   ```

4. Enter a **fictional** password and read the score, issues, and suggestions. Enter `/quit` to exit. `Ctrl+C` or end-of-input also ends the session. The program does not require a real password.
5. Reproduce the included fictional example output:

   ```bash
   python password_analyzer.py --demo
   ```

6. Run the automated test suite:

   ```bash
   python -m unittest -v test_password_analyzer.py
   ```

On computers that use `python3` or `py`, replace `python` in each command accordingly.

## Score and labels

| Positive condition | Points |
| --- | ---: |
| At least 8 characters | 1 |
| At least 12 characters | 1 |
| At least one uppercase letter | 1 |
| At least one lowercase letter | 1 |
| At least one digit | 1 |
| At least one non-alphanumeric symbol | 1 |
| **Maximum** | **6** |

A local-list common password, a run of three repeated adjacent characters, or one of the listed predictable three-character sequences **overrides the points and sets the score to zero**. A score of 0–2 is **Weak**, and 3–4 is **Medium**. A score of 5–6 is **Strong only if** it has at least 12 characters and no flagged issues; otherwise it is **Medium**. A sample with 8–11 characters can meet the minimum demonstration rules but still rate Medium. The tool describes these as **estimated ratings**.

### Examples (invented passwords only)

| Invented input | Expected rating | Main reason |
| --- | --- | --- |
| `abc` | Weak | Short, missing character types, predictable sequence |
| `Password1!` | Weak | On local common-password list |
| `Moooo!85Quill` | Weak | Repeated characters |
| `Abc123!XYzZ` | Weak | Predictable alphabet/number sequences |
| `Aa7!test` | Medium | Meets the minimum rules, but under 12 characters |
| `River!88Maple#Sun` | Strong | Passes the defined educational rules |

These samples are public test strings. **Do not reuse them as real passwords.**

## Code map

- `is_common_password(password)`: local denylist lookup, ignoring case.
- `has_repeated_characters(password)`: compares each consecutive group of three characters.
- `has_predictable_sequence(password)`: checks three-character groups against defined alphabet, digit, and keyboard runs.
- `analyze_password(password)`: applies the six positive criteria and override rules; returns a result dictionary.
- `print_analysis(result)`: displays readable feedback without printing the submitted password.
- `run_demo()`: processes six fixed fictional examples, useful for screenshots.
- `main()`: supports the interactive CLI and `--demo` option.

## Testing and demonstration evidence

Tests cover empty/short input, individual missing categories, case-insensitive common-password matching, repeated characters, sequence types, the override rule, the Medium category, the Strong category, and result privacy. The report includes selected captured output. The `evidence`  were generated from actual runs, not manually typed example outputs.

## Security and limitations

- **Educational, not production strength estimation.** A six-point checklist cannot calculate password entropy, cracking cost, or real security.
- The local list has just 20 examples. It cannot detect most breached passwords, variants, or look-alike character substitutions.
- The pattern detector looks for a small set of sequences and may flag innocuous three-character parts of a word; other predictable patterns may go unnoticed.
- Requiring uppercase/lowercase/digits/symbols is an **assignment demonstration rule**, not a universal best-practice mandate. Length, uniqueness, and avoiding known compromised choices are important.
- User input is processed in memory; it is not saved or sent by this script. However, terminal software, the operating system, or a screen recording may have their own behavior. `getpass()` may warn or fall back in unsupported terminals.
- The strength classification is not a substitute for a password manager, approved authentication controls, multi-factor authentication, or a trusted breach-password checking service.

## AI assistance and authorship disclosure

The project proposal and progress update document use of ChatGPT for clarifying scope, Python loop and list concepts, debugging, and test ideas. Code and documentation have since been reviewed and tested. The report includes **representative prompt examples rather than claimed verbatim transcripts**. 


