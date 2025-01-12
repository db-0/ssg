import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is an HTML Node", None, {"href": "testing.com", "testprop": "blank",})
        node2 = HTMLNode("<p>", "This is an HTML Node", None, {"href": "testing.com", "testprop": "blank",})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("<p>", "This is an HTML Node", "node6", {"href": "testing.com",})
        node2 = HTMLNode("<p>", "This is an HTML Node", None, {"href": "testing.com",})
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode(props={"href": "test.com"})
        leading_space = node.props_to_html()[0]
        self.assertEqual(leading_space, " ")


    def test_leaf_eq(self):
        node = LeafNode("a", "This is a link", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), "<a href=\"https://boot.dev\">This is a link</a>")

    # ParentNode tests
    def test_pn_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()

