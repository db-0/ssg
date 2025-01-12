from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

    parent = ParentNode("div", [
        ParentNode("p", [
            LeafNode("b", "Hello")
        ]),
        LeafNode("i", "World")
    ])

    print(parent.to_html())

main()
