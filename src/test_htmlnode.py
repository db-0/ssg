import unittest

from htmlnode import HTMLNode


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
