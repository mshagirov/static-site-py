import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("Text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", TextType.NORMAL, url=None)
        for t in TextType:
            if t == TextType.NORMAL: continue
            node2 = TextNode("This is a text node", t, url=None)
            self.assertNotEqual(node, node2)


    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        node3 = TextNode("This is a text node", TextType.BOLD, url="https://www.example.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()
