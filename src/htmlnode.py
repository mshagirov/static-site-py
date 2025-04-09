"""
HTMLNode module
"""

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        '''
        Args:
        - tag:str : HTML tag, e.g., "img", "a", "p" for <img>, <a> and <p>. 
        - value:str : text content of a node.
        - children:list : list of child HTML nodes, children may contain grandchild nodes
        - props:dict : dictionary of node properties (strings) e.g., {"href": "https://www.example.com"}.
        '''

        self.tag = tag
        self.value =value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        '''
        Child classes should override this method
        '''
        raise(Exception("NotImplementedError"))

    def props_to_html(self) -> str:
        '''
        Returns a string representation of the HTML attributes of the node
        '''
        if self.props is None:
            return ""
        return " " + " ".join([f'{k}="{self.props[k]}"' for k in self.props])

    def __repr__(self) -> str:
       return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})" 
