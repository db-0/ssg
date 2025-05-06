import unittest

from textnode import *
from textconversion import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_url_eq(self):
        node1 = TextNode("Test text node", TextType.LINK, None)
        node2 = TextNode("Test text node", TextType.LINK)
        self.assertEqual(node1, node2)

    def test_type_noteq(self):
        node1 = TextNode("Test text node", TextType.CODE)
        node2 = TextNode("Test text node", TextType.LINK)
        self.assertNotEqual(node1, node2)
    
    def test_url_noteq(self):
        node1 = TextNode("Test text node", TextType.CODE, "https://boot.dev")
        node2 = TextNode("Test text node", TextType.CODE, None)
        self.assertNotEqual(node1, node2)

    def test_normal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
    
    def test_link(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is an image node"})

class TestTextConversion(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a **bold** node.", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), 
                         [TextNode("This is a ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None),
                          TextNode(" node.", TextType.TEXT, None)])

if __name__ == "__main__":
    unittest.main()
