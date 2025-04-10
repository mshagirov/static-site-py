import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md = '\n# This is Title   \n\n## Subheading\n\nContents\n'
        h1 = extract_title(md)
        self.assertEqual(h1, "This is Title")

    def test_exception(self):
        md = "\n## h2 heading\n\n> quote with `code`\n\nText block."
        with self.assertRaises(Exception):
            extract_title(md)

    def test_wrong_order(self):
        md = "\n### h3\n\n## h2\n\n#not h1\n\n#  space padded h1  \n"
        h1 = extract_title(md)
        self.assertEqual(h1, "space padded h1")

if __name__ == "__main__":
   unittest.main() 
