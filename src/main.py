from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test)
    
    test2 = HTMLNode(props={"href": "test.com", "target": "_blank",})
    print(test2.props_to_html())

    print(repr(test2))

main()
