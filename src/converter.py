"""
Module for converting raw text and TextNode to HTMLNode conversion function
"""
from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node:TextNode):
    '''
    Converts TextNode to LeafNode
    '''

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url,
                                              "alt": text_node.text})
        case _:
            raise(Exception("text_node should be one of TextType types"))

def split_nodes_delimeter(old_nodes:list, delimeter:str, text_type:TextType):
    '''
    Splits input "old_nodes" using "delimeter" and a "text_type" 

    E.g.:

        old_node = TextNode("This is text with a `code block` word", TextType.TEXT)
    
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)

    Returns:
        [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        ]
    '''
    new_nodes = []
    for node in old_nodes:
        for k,part in enumerate(node.text.split(delimeter)):
            if k%2==0:
                new_nodes.append(TextNode(part, node.text_type))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text:str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text:str):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

