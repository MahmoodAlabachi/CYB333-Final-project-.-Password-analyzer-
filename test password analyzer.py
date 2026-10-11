"""Standard-library regression tests for the Password Strength Analyzer."""

import unittest

from password_analyzer import (
    analyze_password,
    has_predictable_sequence,
    has_repeated_characters,
    is_common_password,
)


class PasswordAnalyzerTests(unittest.TestCase):
    """Verify scoring, minimum rules, common inputs, and pattern overrides."""

    def test_empty_password_is_weak(self):
        result = analyze_password("")
        self.assertEqual((result["score"], result["rating"]), (0, "Weak"))
        self.assertFalse(result["meets_minimum_rules"])

    def test_too_short_has_length_issue(self):
        self.assertTrue(any("8 characters" in msg for msg in analyze_password("Ab7!")["issues"]))

    def test_missing_uppercase(self):
        self.assertTrue(any("uppercase" in msg for msg in analyze_password("river!88maple")["issues"]))

    def test_missing_lowercase(self):
        self.assertTrue(any("lowercase" in msg for msg in analyze_password("RIVER!88MAPLE")["issues"]))

    def test_missing_digit(self):
        self.assertTrue(any("number" in msg for msg in analyze_password("River!MapleSun")["issues"]))

    def test_missing_symbol(self):
        self.assertTrue(any("symbol" in msg for msg in analyze_password("River88MapleSun")["issues"]))

    def test_local_common_list_ignores_case(self):
        self.assertTrue(is_common_password("PaSsWoRd1!"))
        self.assertEqual(analyze_password("PaSsWoRd1!")["score"], 0)

    def test_unknown_password_not_falsely_in_small_denylist(self):
        self.assertFalse(is_common_password("River!88Maple#Sun"))

    def test_repeated_characters_are_found(self):
        self.assertTrue(has_repeated_characters("AaAA7!test"))
        self.assertEqual(analyze_password("Moooo!85Quill")["rating"], "Weak")

    def test_no_repeated_characters(self):
        self.assertFalse(has_repeated_characters("River!88Maple#Sun"))

    def test_ascending_digit_sequence(self):
        self.assertTrue(has_predictable_sequence("Abc!789Xyz"))

    def test_descending_digit_sequence(self):
        self.assertTrue(has_predictable_sequence("Ab!987xyz"))

    def test_alphabet_sequence(self):
        self.assertTrue(has_predictable_sequence("Z!stuv66"))

    def test_keyboard_sequence(self):
        self.assertTrue(has_predictable_sequence("A!qwe88B"))

    def test_sequence_overrides_other_positive_criteria(self):
        result = analyze_password("Abc123!XYzZ")
        self.assertEqual(result["score"], 0)
        self.assertEqual(result["rating"], "Weak")

    def test_medium_for_8_to_11_characters(self):
        result = analyze_password("Aa7!test")
        self.assertEqual(result["score"], 5)
        self.assertEqual(result["rating"], "Medium")
        self.assertTrue(result["meets_minimum_rules"])

    def test_strong_fictional_password(self):
        result = analyze_password("River!88Maple#Sun")
        self.assertEqual(result["score"], 6)
        self.assertEqual(result["rating"], "Strong")
        self.assertEqual(result["issues"], [])

    def test_analysis_does_not_print_the_password(self):
        # Logic returns classifications without displaying or storing the input.
        result = analyze_password("River!88Maple#Sun")
        self.assertNotIn("River!88Maple#Sun", str(result))


if __name__ == "__main__":
    unittest.main()
