from enum import Enum

class TextType(Enum):
    TEXT = 'text' # TextType.TEXT
    BOLD = 'bold'   # TextType.BOLD
    ITALIC = 'italic' # TextType.ITALIC
    CODE = 'code'   # TextType.CODE
    LINK = 'link'   # TextType.LINK
    IMAGE = 'image' # TextType.IMAGE

class TextNode:
    def __init__(self, text, text_type, url=None):
        assert text_type in TextType

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        '''
        True if attributes of the other object are equal self
        '''
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type}{", " + self.url if self.url != None else ""})'


