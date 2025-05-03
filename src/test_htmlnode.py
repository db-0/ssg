import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_exception_in_child(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError) as error:
            node = parent_node.to_html()
        self.assertEqual("all parent nodes must have a tag", str(error.exception))
