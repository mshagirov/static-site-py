
import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None,[LeafNode(None, "Normal text")]).to_html()

    def test_to_html_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p",None).to_html()

    def test_to_html_with_child(self):
        child = LeafNode("b", "Click me button!")
        parent = ParentNode("button", [child], {"type":"button", "class":"btn"})
        self.assertEqual(parent.to_html(), '<button type="button" class="btn"><b>Click me button!</b></button>')

    def test_to_html_with_children(self):
        child = LeafNode("b", "Click me button!")
        self.assertEqual(ParentNode("p", [child, child, child]).to_html(),
                         '<p><b>Click me button!</b><b>Click me button!</b><b>Click me button!</b></p>')

    def test_to_html_grandchild(self):
        grandchild = LeafNode("p", "grandchild")
        child = ParentNode("span", [grandchild])
        self.assertEqual(ParentNode("div",[child]).to_html(),
                         '<div><span><p>grandchild</p></span></div>')
    
if __name__ == "__main__":
    unittest.main()
