import unittest
from converter import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestSplitNodes(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a link ", TextType.TEXT),
                              TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                              TextNode(" and ", TextType.TEXT),
                              TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
                              ],
                             new_nodes)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                              TextNode(" and another ", TextType.TEXT),
                              TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                              ],
                             new_nodes)

    def test_split_image_link(self):
        node = TextNode(
            "This is text part and [link_alt](https://link.url.com) and ![image_alt_text](https://image.source.com/123.png) some other text",
            TextType.TEXT
        )
        img_then_link = split_nodes_link(split_nodes_image([node]))
        link_then_img = split_nodes_image(split_nodes_link([node]))
        self.assertEqual(img_then_link, link_then_img)
        self.assertEqual(
            [
                TextNode("This is text part and ", TextType.TEXT),
                TextNode("link_alt", TextType.LINK, "https://link.url.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image_alt_text", TextType.IMAGE, "https://image.source.com/123.png"),
                TextNode(" some other text", TextType.TEXT),
            ]
            , img_then_link) 

    def test_empty_node(self):
        node  = TextNode( "", TextType.TEXT)
        self.assertEqual( [ TextNode("", TextType.TEXT) ], 
                         split_nodes_image(split_nodes_link([node])))

    def test_image_double_split(self):
        node = TextNode("This is text part ![img_alt_text](https://image.source.com/123.png)", TextType.TEXT)
        new_nodes  = split_nodes_image( split_nodes_image( [ node] ) )
        self.assertEqual(
            [ 
                TextNode("This is text part ", TextType.TEXT),
                TextNode("img_alt_text", TextType.IMAGE, "https://image.source.com/123.png")
            ],
            new_nodes
        )

    def test_link_double_split(self):
        node = TextNode("This is text part [link_text](https://image.source.com/123.png)", TextType.TEXT)
        new_nodes  = split_nodes_link( split_nodes_link( [ node] ) )
        self.assertEqual(
            [ 
                TextNode("This is text part ", TextType.TEXT),
                TextNode("link_text", TextType.LINK, "https://image.source.com/123.png")
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()

