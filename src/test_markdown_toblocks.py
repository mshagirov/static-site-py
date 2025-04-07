import unittest
from converter import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ])
    def test_empty_lines(self):
        md = " \n# h1\n\n\n## h2\n\nSome _text_. Somemore **text** here.\n\n\n\n\nLast paragraph\n"
        blocks =markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                '# h1', '## h2', 'Some _text_. Somemore **text** here.', 'Last paragraph'
            ]
        )

    


if __name__ == "__main__":
    unittest.main()
