import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_novalue(self):
        node_no_value = HTMLNode(children=[HTMLNode(value=f"Node {k}") for k in range(3)])
        # An HTMLNode without a value will be assumed to have children
        self.assertTrue((not node_no_value.value) and node_no_value.children)

    def test_nochildren(self):
        node_no_child = HTMLNode(value=f"This is text")
        # An HTMLNode without children will be assumed to have a value
        self.assertTrue((not node_no_child.children) and node_no_child.value)

    def test_props(self):
        node_no_prop = HTMLNode(props=None)
        self.assertTrue(node_no_prop.props is None)
        self.assertEqual(node_no_prop.props_to_html(), "")

        node_prop = HTMLNode(props={"href": "https://www.example.com",
                                    "target": "_blank"})
        node_prop2 = HTMLNode(props={"type": "video/webm",
                                     "data":"https://www.example.net/media/videos/video.webm",
                                     "width":"600",
                                     "height":"140"})
        self.assertFalse(node_prop.props is None)
        self.assertEqual(node_prop.props_to_html(), ' href="https://www.example.com" target="_blank"')
        self.assertEqual(node_prop2.props_to_html(),
                         ' type="video/webm" data="https://www.example.net/media/videos/video.webm" width="600" height="140"')
        # An HTMLNode without props simply won't have any attributes

if __name__ == "__main__":
    unittest.main()
