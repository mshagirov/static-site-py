import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p",None).to_html()

    def test_leaf_to_html_p(self):
        self.assertEqual(LeafNode("p","This is a paragraph.").to_html(),
                         "<p>This is a paragraph.</p>")

    def test_leaf_to_html_a(self):
        self.assertEqual(LeafNode("a", "Click me button!", {"href": "https://www.example.com"}).to_html(),
                         '<a href="https://www.example.com">Click me button!</a>'
                         )
    
if __name__ == "__main__":
    unittest.main()
