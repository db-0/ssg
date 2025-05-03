from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node is not isinstance(TextType.TEXT):
            new_nodes.append(node)
        splits = node.split(delimiter)
        for split in splits:
            