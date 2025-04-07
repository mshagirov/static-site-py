from enum import Enum
import re

class BlockType(Enum):
    paragraph = 'paragraph' # texttype.text
    heading = 'heading'   # texttype.bold
    code = 'code' # texttype.italic
    quote = 'quote'   # texttype.code
    unordered_list = 'unordered_list'   # texttype.link
    ordered_list = 'ordered_list' # texttype.image

def block_to_block_type(block:str)->BlockType:
    if re.match(r"^(#){1,6}(\s)",block):
        return BlockType.heading

    elif re.search(r"^```[^`][\s\S]*[^`]```$", block):
        return BlockType.code

    elif all(map(lambda line: line[:1]==">", block.split("\n"))):
        return BlockType.quote

    elif all(map(lambda line: line[:2]=="- ", block.split("\n"))):
        return BlockType.unordered_list

    elif all(map(lambda line: re.search(r"^\d+(\.){1}(\s){1}",line),  block.split("\n"))):
        lines = block.split("\n")
        is_ordered = list( map( lambda line: int(line.split(". ")[0]), lines)) == \
                     list( range( 1, len(lines)+1))

        return BlockType.ordered_list if is_ordered else BlockType.paragraph

    else:
        return BlockType.paragraph

