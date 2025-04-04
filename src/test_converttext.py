import unittest
from textnode import TextType, TextNode
from converter import text_node_to_html_node

class TestConvertText(unittest.TestCase):
    def test_text(self):
        text = "This is a text node"
        tags = {TextType.TEXT : None,
                TextType.BOLD : "b",
                TextType.ITALIC : "i",
                TextType.CODE : "code" }
        for text_type in tags:
            node = TextNode(text, text_type)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, tags[text_type])
            self.assertEqual(html_node.value, text )

    def test_link(self):
        text = "This is a text node"
        url = "https://www.example.com"
        node = TextNode(text, TextType.LINK, url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, text )
        self.assertEqual(html_node.props, {"href": url})

    def test_image(self):
        text = "This is a text node"
        url = "media/images/1.png"
        node = TextNode(text, TextType.IMAGE, url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "" )
        self.assertEqual(html_node.props, {"src": url, "alt":text})


if __name__ == "__main__":
    unittest.main()
