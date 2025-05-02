import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
