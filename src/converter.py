"""
Raw text, TextNode, and HTMLNode conversion functions
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
        if (node.text_type == TextType.LINK) or (node.text_type == TextType.IMAGE):
            new_nodes.append(node)
            continue

        for k,part in enumerate(node.text.split(delimeter)):
            if (k%2==0) and part:
                new_nodes.append(TextNode(part, node.text_type))
            elif part:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text:str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text:str):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

def split_nodes_link(old_nodes:list):
    def split_at_link(text:str,link:tuple):
        return text.split(f"[{link[0]}]({link[1]})", 1)
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        for link in links:
            before_after = split_at_link(text, link)
            if before_after[0]:
                new_nodes.append( TextNode(before_after[0], node.text_type, node.url))
            new_nodes.append( TextNode(link[0], TextType.LINK, link[1]) )
            text = before_after[1]
        if text:
            new_nodes.append( TextNode( text, node.text_type, node.url))

    return new_nodes


def split_nodes_image(old_nodes:list):
    def split_at_image(text:str,image:tuple):
        return text.split(f"![{image[0]}]({image[1]})", 1)
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        text = node.text
        for image in images:
            before_after = split_at_image(text, image)
            if before_after[0]:
                new_nodes.append( TextNode(before_after[0], node.text_type, node.url))
            new_nodes.append( TextNode(image[0], TextType.IMAGE, image[1]) )
            text = before_after[1]
        if text:
            new_nodes.append( TextNode( text, node.text_type, node.url))

    return new_nodes


def text_to_textnodes(text:str):
    # node = TextNode(text, TextType.TEXT)
    types_delim = {TextType.BOLD : "**", TextType.ITALIC:"_", TextType.CODE:"`"}
    nodes = [ TextNode(text, TextType.TEXT)]

    nodes = split_nodes_link(split_nodes_image(nodes))

    for t in types_delim:
        nodes  = split_nodes_delimeter(nodes, types_delim[t], t)

    return nodes

def markdown_to_blocks(markdown:str):
    blocks = markdown.split("\n\n")
    blocks = list(filter( len, map(lambda block: block.strip(), blocks)))
    return blocks

