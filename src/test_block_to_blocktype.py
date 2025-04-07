import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(BlockType.paragraph, block_to_block_type(""))
        self.assertEqual(BlockType.paragraph, block_to_block_type("Some paragraph\nline 2"))

    def test_headings(self):
        for h_k in range(1,7):
            text = h_k*"#" + f" heading {h_k}"
            self.assertEqual(BlockType.heading, block_to_block_type(text))
        not_h1 = "not # heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(not_h1))
        not_h7 = "#"*7 + " not a heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(not_h7))
        not_h0 = "#not a heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(not_h0))

    def test_code(self):
        code_text = """```code line 1\ncode line 2\ncode line 3\n```"""
        self.assertEqual(BlockType.code, block_to_block_type(code_text))
        # not code:
        self.assertEqual(BlockType.paragraph, block_to_block_type(code_text + '`'))
        self.assertEqual(BlockType.paragraph, block_to_block_type('`' + code_text))

    def test_quote(self):
        quote = "> line 1\n> line 2\n>line 3" # note that line 3 has not space between ">" and "l"
        self.assertEqual( BlockType.quote, block_to_block_type(quote))

        not_quote = "> line 1\n- line 2"
        self.assertEqual( BlockType.paragraph, block_to_block_type(not_quote) )
        
        not_quote2 = "> line 1\nline 2 w/ wrong > placement"
        self.assertEqual( BlockType.paragraph, block_to_block_type(not_quote2) )

    def test_ulist(self):
        text = "- item 1\n- item 2\n- item 3"
        self.assertEqual( BlockType.unordered_list, block_to_block_type(text) )

        not_ulist ="- item 1\n-item 2"
        self.assertEqual( BlockType.paragraph, block_to_block_type(not_ulist))

    def test_olist(self):
        text = "1. item 1\n2. item 2\n3. item 3\n4. item 4"
        self.assertEqual( BlockType.ordered_list, block_to_block_type(text))

        long_olist = "\n".join([f"{k}. item {k}" for k in range(1,21)])
        self.assertEqual( BlockType.ordered_list, block_to_block_type( long_olist) )

        not_olist = "1. item 1\n2.item2"
        self.assertEqual( BlockType.paragraph, block_to_block_type(not_olist))
        
        not_ordered = "1. item 1\n2. item 2\n4. item 3"
        self.assertEqual( BlockType.paragraph, block_to_block_type(not_ordered))

        start_wzero = "0. item 0\n1. item 1"
        self.assertEqual( BlockType.paragraph, block_to_block_type( start_wzero) )

if __name__ == "__main__":
    unittest.main()
