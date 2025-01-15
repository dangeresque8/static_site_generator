import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_None(self):
        node1 = HTMLNode()
        self.assertIsNone(node1.tag)
        self.assertIsNone(node1.value)
        self.assertIsNone(node1.children)
        self.assertIsNone(node1.props)

    def test_eq(self):
        node1 = HTMLNode("p", "test goes here", ["list", "of", "children"], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("p", "test goes here", ["list", "of", "children"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node1.__repr__(), node2.__repr__())

    def test_string(self):
        node1 = HTMLNode("p", "test goes here", ["list", "of", "children"], {"href": "https://www.google.com", "target": "_blank",})
        bol = isinstance(node1.props_to_html(), str)
        self.assertTrue(bol)



if __name__ == "__main__":
    unittest.main()