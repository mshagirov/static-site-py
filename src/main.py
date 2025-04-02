from textnode import TextNode, TextType

def main():
    text_node_obj =  TextNode("Alt text", TextType.IMAGE, url="./image1.png")
    print(text_node_obj)


if __name__ == '__main__':
    # excute when called from CLI
    main()
