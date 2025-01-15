
from textnode import TextNode, TextType
from htmlnode import HTMLNode

print("hello world")



def main():
    # test1 = TextNode("example text", TextType.BOLD, "www.fake.com")
    # print(test1)
    HTMLNode_dict = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    test2 = HTMLNode("p", "test goes here", ["list", "of", "children"], HTMLNode_dict)
    print(test2)
main()