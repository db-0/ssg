from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            result = []

            while delimiter in text:
                start_index = text.find(delimiter)
                result.append(TextNode(text[:start_index], TextType.TEXT))
                end_index = text.find(delimiter, start_index + len(delimiter))
                if end_index == -1:
                    raise Exception("no closing delimiter found")
                result.append(TextNode(text[start_index + len(delimiter):end_index], text_type))
                text = text[end_index + len(delimiter):]
            
            if text:
                result.append(TextNode(text, TextType.TEXT))
            new_nodes.extend(result)

    return new_nodes
