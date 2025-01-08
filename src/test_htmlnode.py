import unittest
from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()

