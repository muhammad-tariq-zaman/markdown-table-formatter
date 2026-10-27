import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestFormatter(unittest.TestCase):
    def test_columns_aligned(self):
        text = "# T\n| Name | Age |\n|---|---|\n| Ali | 30 |\n| Muhammad Tariq | 24 |\n"
        out = main.format_text(text)
        lines = [l for l in out.splitlines() if l.startswith("|")]
        pipes = [l.count("|") for l in lines]
        self.assertTrue(all(n == pipes[0] for n in pipes))
        self.assertIn("Muhammad Tariq", out)
        self.assertIn("| Name", out)

    def test_non_table_lines_kept(self):
        self.assertIn("hello", main.format_text("hello\n"))


if __name__ == "__main__":
    unittest.main()
