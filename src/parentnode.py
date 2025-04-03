"""
ParentNode module
"""

from htmlnode import HTMLNode
# from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise(ValueError("ParentNode must have a tag"))
        if (self.children == None) or (not self.children):
            raise(ValueError("ParentNode must have child nodes"))
        
        return f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda x: x.to_html(),self.children))}</{self.tag}>'



