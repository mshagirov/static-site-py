import re

from blocktype import BlockType, block_to_block_type
from converter import markdown_to_blocks, text_node_to_html_node, text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType

def markdown_to_html_node(markdown:str)->ParentNode:
    '''
    Convert markdown text to a single parent HTML node.
    '''
    def text_to_children(text)->list:
        text = text.replace("\n", " ")
        return list( map( text_node_to_html_node, text_to_textnodes( text ) ) )

    def text_to_heading_level(text)->int:
        level = 1
        matches = re.match(r"^#+", text)
        if matches:
            level = len(matches.group())
        return level

    def text_to_li_prefix(text):
        prefix_match = re.match(r"^\d+(\.){1}(\s){1}", text)
        return prefix_match.group()  if prefix_match!=None else "- "

    def text_to_list_items(text)->list:
        list_items = list(
            map(
                lambda line: line[len(text_to_li_prefix(line)):], text.split("\n")
            )
        )
        return list_items

    def list_items_to_children(list_items)->list:
        list_nodes = list(
            map(
                lambda item: ParentNode("li", text_to_children(item)), list_items 
            )
        )
        return list_nodes
    
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.paragraph:
                children.append(
                    ParentNode( "p", text_to_children(block))
                )
            case BlockType.heading:
                h_level = text_to_heading_level(block)
                children.append(
                    ParentNode( f"h{h_level}", text_to_children(block[h_level+1:]) )
                )
            case BlockType.code:
                block = block.strip("`")
                if block[:1] == "\n":
                    block = block[1:]
                children.append(
                    ParentNode("pre", [text_node_to_html_node( TextNode( block, TextType.CODE) )] )
                )
            case BlockType.quote:
                block = " ".join(
                    map(lambda line: line[1:].strip(), block.split("\n"))
                )
                children.append(
                    ParentNode("blockquote", text_to_children(block)) 
                )
            case BlockType.unordered_list:
                list_items = text_to_list_items(block)
                list_nodes = list_items_to_children(list_items)
                children.append( 
                    ParentNode("ul", list_nodes ) 
                )
            case BlockType.ordered_list:
                list_items = text_to_list_items(block)
                list_nodes = list_items_to_children(list_items)

                children.append(
                    ParentNode("ol", list_nodes)
                )
    # combine children in to one parent <div> node
    return ParentNode("div", children)

