"""Password Strength Analyzer: educational, offline password-rule checker.

The analyzer evaluates invented sample passwords against transparent rules.
Its strength label is an estimate, not a measure of resistance to attacks.
No input password is written to a file or transmitted by this program.
"""

import argparse
from getpass import getpass


# A deliberately small, local collection used to illustrate denylist checks.
# This is NOT a comprehensive list of leaked or frequently used passwords.
COMMON_PASSWORDS = frozenset(
    {
        "password", "123456", "qwerty", "abc123", "letmein", "monkey",
        "dragon", "111111", "baseball", "iloveyou", "password1!",
        "welcome1!", "qwerty123!", "admin123!", "letmein1!",
        "football1!", "sunshine1!", "monkey123!", "dragon123!",
        "baseball1!",
    }
)

# Three consecutive characters from any of these runs are predictable.
# Checks are illustrative and focus on ASCII alphabet, digits, and keyboards.
SEQUENCE_RUNS = (
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
    "0123456789",
    "9876543210",
    "qwertyuiop",
    "poiuytrewq",
    "asdfghjkl",
    "lkjhgfdsa",
    "zxcvbnm",
    "mnbvcxz",
)


def is_common_password(password):
    """Return True if the entire password matches the small local denylist.

    Matching is case-insensitive so changing capitalization alone does not
    disguise a listed password. Partial matches are not considered.
    """
    return password.casefold() in COMMON_PASSWORDS


def has_repeated_characters(password):
    """Detect a run of three identical adjacent characters (ignoring case)."""
    normalized = password.casefold()
    return any(
        normalized[index] == normalized[index + 1] == normalized[index + 2]
        for index in range(len(normalized) - 2)
    )


def has_predictable_sequence(password):
    """Detect any three-character ascending, descending, or keyboard run."""
    normalized = password.casefold()
    for index in range(len(normalized) - 2):
        group = normalized[index:index + 3]
        if any(group in sequence for sequence in SEQUENCE_RUNS):
            return True
    return False


def analyze_password(password):
    """Return a score, estimated rating, issues, and suggestions.

    The six positive criteria award one point each: length >= 8, length >= 12,
    uppercase, lowercase, digit, and non-alphanumeric symbol. A common
    password, three repeated characters, or a predictable sequence sets
    the score to zero. A Strong rating also requires 12+ characters and no
    outstanding issues; an 8-11 character valid entry can be Medium.
    """
    has_uppercase = any(character.isupper() for character in password)
    has_lowercase = any(character.islower() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_symbol = any(not character.isalnum() for character in password)

    criteria = (
        len(password) >= 8,
        len(password) >= 12,
        has_uppercase,
        has_lowercase,
        has_digit,
        has_symbol,
    )
    score = sum(criteria)
    issues = []

    if len(password) < 8:
        issues.append("Use at least 8 characters to meet the demonstration minimum.")
    if not has_uppercase:
        issues.append("Include at least one uppercase letter.")
    if not has_lowercase:
        issues.append("Include at least one lowercase letter.")
    if not has_digit:
        issues.append("Include at least one number.")
    if not has_symbol:
        issues.append("Include at least one symbol.")

    # Predictable patterns override the positive points: variety is not enough.
    if is_common_password(password):
        issues.append("This password appears on the small local common-password list.")
        score = 0
    if has_repeated_characters(password):
        issues.append("Avoid three or more repeated adjacent characters.")
        score = 0
    if has_predictable_sequence(password):
        issues.append("Avoid sequences such as abc, 123, 321, or qwe.")
        score = 0

    if score >= 5 and len(password) >= 12 and not issues:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    suggestions = []
    if len(password) < 12:
        suggestions.append("For a stronger choice, use a longer, less predictable passphrase.")
    if issues:
        suggestions.append("Address the listed issues and test a NEW fictional sample.")
    if not issues and rating == "Strong":
        suggestions.append("Passing these rules is not proof of real-world security.")

    return {
        "score": score,
        "maximum_score": 6,
        "rating": rating,
        "meets_minimum_rules": not issues,
        "issues": issues,
        "suggestions": suggestions,
    }


def print_analysis(result):
    """Display one analysis using readable, consistently labeled output."""
    print(f"Password strength: {result['rating']}")
    print(f"Score: {result['score']}/{result['maximum_score']}")
    if result["issues"]:
        print("Issues:")
        for issue in result["issues"]:
            print(f"  - {issue}")
    else:
        print("All demonstration minimum requirements are met.")
    if result["suggestions"]:
        print("Suggestions:")
        for suggestion in result["suggestions"]:
            print(f"  - {suggestion}")


def run_demo():
    """Show reproducible results using only deliberately invented examples."""
    samples = (
        ("Short and predictable", "abc"),
        ("Known local-list example", "Password1!"),
        ("Repeated character example", "Moooo!85Quill"),
        ("Sequential example", "Abc123!XYzZ"),
        ("Valid but short", "Aa7!test"),
        ("Longer fictional sample", "River!88Maple#Sun"),
    )
    for position, (description, sample) in enumerate(samples, start=1):
        print(f"\nSample {position}: {description} (invented test input)")
        print_analysis(analyze_password(sample))


def main():
    """Run the CLI; do not echo entered passwords on supported terminals."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--demo", action="store_true", help="Run with built-in fictional examples."
    )
    args = parser.parse_args()

    print("Password Strength Analyzer (educational demonstration)")
    print("Use only fictional passwords; never enter a real account password.")
    if args.demo:
        run_demo()
        return

    while True:
        try:
            password = getpass("\nEnter fictional password (/quit to exit): ")
        except (EOFError, KeyboardInterrupt):
            print("\nSession ended.")
            break
        if password == "/quit":
            print("Session ended.")
            break
        print_analysis(analyze_password(password))


if __name__ == "__main__":
    main()
