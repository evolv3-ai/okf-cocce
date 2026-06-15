import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "tools" / "validate-okf-cocce.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

class ValidatorTests(unittest.TestCase):
    def test_repository_validates(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_missing_type_is_error(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bad.md"
            p.write_text("---\ntitle: Bad\n---\nBody\n", encoding="utf-8")
            with self.assertRaises(validator.ValidationError):
                validator.parse_frontmatter(p)

    def test_broken_link_is_error(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            p = root / "doc.md"
            p.write_text("See [missing](missing.md).", encoding="utf-8")
            with self.assertRaises(validator.ValidationError):
                validator.validate_links(root, p, p.read_text())

if __name__ == "__main__":
    unittest.main()
