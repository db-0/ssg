import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", None, None, None)
        node2 = HTMLNode("p", None, None, None)
        self.assertEqual(node1, node2)
    
    def test_eq_propstohtml(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        props_text = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), props_text)
    
    def test_noteq(self):
        node1 = HTMLNode("p", "Test", None, None)
        node2 = HTMLNode("p", None, None, None)
        self.assertNotEqual(node1, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError) as error:
            node = LeafNode("b", None, None).to_html()
        self.assertEqual("all leaf nodes must have a value", str(error.exception))
