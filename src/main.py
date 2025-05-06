from textnode import *
from htmlnode import *
from textconversion import *


def main():

    
    node = TextNode("This is a **bold** node.", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

if __name__ == "__main__":
    main()
