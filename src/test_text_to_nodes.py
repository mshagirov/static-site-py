import unittest
from converter import text_to_textnodes
from textnode import TextType, TextNode

class TestTextToTextNodes(unittest.TestCase):
    def test_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual([ 
            TextNode("This is ", TextType.TEXT), 
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
                         nodes)
    def test_nested_text(self):
        text = "A **text**, _italic words_ `code block` ![sample image](https://img.com/123.jpeg) [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("A ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(", ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("sample image", TextType.IMAGE, "https://img.com/123.jpeg"),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            nodes
        )


if __name__ == "__main__":
    unittest.main()
