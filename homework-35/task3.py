from abc import ABC, abstractmethod
import re


class Node:
    def __init__(self, tag, attributes=None, text=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.text = text
        self.parent = None
        self.children = []

    def __str__(self, indent=0):
        result = ' ' * indent + f'<{self.tag}'

        if self.attributes:
            result += f" {' '.join([f'{key}={value}' for key, value in self.attributes.items()])}"

        result += '>\n'

        for child in self.children:
            result += child.__str__(indent + 2)

        if self.text:
            result += ' ' * (indent + 2) + f'{self.text}\n'

        result += ' ' * indent + f'</{self.tag}>\n'

        return result

    def __repr__(self):
        return f'<Node object; tag={self.tag}, attributes={self.attributes}, children={self.children}>'


class SaxParser(ABC):
    def tag_info(self, tag):
        tag_match = re.match(r'([a-zA-Z]+)(.*)', tag)
        tag_name, attrs_str = tag_match.groups()

        attrs = dict(re.findall(r'([a-zA-Z]+)="([^"]*)"', attrs_str))

        return tag_name, attrs

    def parse(self, html):
        pattern = r'<(/?[a-zA-Z]+).*?>|([^<]+)'
        matches = re.finditer(pattern, html)

        data_stack = []
        root = None

        for match in matches:
            tag, text = match.groups()

            if tag:
                if tag.startswith('/'):
                    self.end_tag(data_stack, tag[1:])
                else:
                    tag_name, attrs = self.tag_info(tag)
                    node = self.start_tag(tag_name, attrs)

                    if not root:
                        root = node

                    data_stack.append(node)

            elif text:
                self.data(data_stack, text)

        if len(data_stack) > 1:
            raise ValueError('More than one root tag found.')

        return root

    @abstractmethod
    def start_tag(self, tag, attrs):
        pass

    @abstractmethod
    def end_tag(self, stack, tag):
        pass

    @abstractmethod
    def data(self, stack, text):
        pass


class MySaxParser(SaxParser):
    def __init__(self):
        super().__init__()
        self.data_stack = []

    def start_tag(self, tag, attrs):
        node = Node(tag, attrs)

        if self.data_stack:
            node.parent = self.data_stack[-1]
            self.data_stack[-1].children.append(node)

        return node

    def end_tag(self, stack, tag):
        if not stack:
            raise ValueError(f'Closing tag "{tag}" with no corresponding opening tag.')

        if stack[-1].tag != tag:
            raise ValueError(f'Closing tag "{tag}" does not match the last opened tag "{stack[-1].tag}".')

        stack.pop()

    def data(self, stack, text):
        if stack:
            text_node = Node('#text', text=text)
            stack[-1].children.append(text_node)

def parse_html(html):
    parser = MySaxParser()

    return parser.parse(html)

html_code = """
<html>
  <body bgcolor="red">
    <h1 id="first-header">My First Heading</h1>
    <p topmargin="12">My first paragraph.</p>
  </body>
</html>
"""

root = parse_html(html_code)
print(repr(root))
print(root)
