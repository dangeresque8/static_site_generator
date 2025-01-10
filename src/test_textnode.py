import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        test = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(test.url, None)

    def test_text_not_equal(self):
        test1 = TextNode("text here", TextType.BOLD)
        test2 = TextNode("text here", TextType.ITALIC)
        self.assertNotEqual(test1.text_type, test2.text_type)
    
    def test_object_not_equal(self):
        test1 = TextNode("text goes here", TextType.BOLD)
        test2 = TextNode("text also goes here", TextType.ITALIC)
        self.assertNotEqual(test1, test2)


if __name__ == "__main__":
    unittest.main()