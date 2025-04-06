import unittest
from textnode import TextType, TextNode
from converter import split_nodes_delimeter

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)

    def empty_node(self):
        node = TextNode("****``__", TextType.TEXT)
        nodes = split_nodes_delimeter(
                    split_nodes_delimeter(
                        split_nodes_delimeter( [node], "`", TextType.CODE),
                        "_", TextType.ITALIC),
                    "**", TextType.BOLD)
        answer = [TextNode("", TextType.TEXT),
                  TextNode("", TextType.BOLD),
                  TextNode("", TextType.TEXT),
                  TextNode("", TextType.CODE),
                  TextNode("", TextType.TEXT),
                  TextNode("", TextType.ITALIC),
                  TextNode("", TextType.TEXT)]
        self.assertEqual(nodes, answer)

if __name__ == "__main__":
    unittest.main()
