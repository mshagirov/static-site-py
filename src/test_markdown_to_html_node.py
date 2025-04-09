import unittest
from markdown_to_html_node import markdown_to_html_node

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = '\n> Some Quote\n>continuing the same quote\n\n> This is a new quote\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>Some Quote continuing the same quote</blockquote><blockquote>This is a new quote</blockquote></div>'
        )

    def test_headerblock(self):
        md = """
# h1

## h2

### h3

#### h4

##### h5

###### h6

####### h7 is not a header
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>h1</h1><h2>h2</h2><h3>h3</h3><h4>h4</h4><h5>h5</h5><h6>h6</h6><p>####### h7 is not a header</p></div>'
        )

    def test_inline_link(self):
        md = '\nThis is a [link to wiki page about tux](https://en.wikipedia.org/wiki/Tux_%28mascot%29)\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a <a href="https://en.wikipedia.org/wiki/Tux_%28mascot%29">link to wiki page about tux</a></p></div>'
        )

    def test_image(self):
        md = '\n![This is a picture of a tux](https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg)\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p><img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="This is a picture of a tux"></img></p></div>'
        )

    def test_unorderedlist(self):
        md = '\n- item A\n- item B\n- item C\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>item A</li><li>item B</li><li>item C</li></ul></div>'
        )

    def test_orderedlist(self):
        md = '\n1. item 1\n2. item 2\n3. item 3\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                '<div><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>'
        )

if __name__ == "__main__":
    unittest.main()
