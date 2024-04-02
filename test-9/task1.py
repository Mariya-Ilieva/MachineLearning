import re


def parse_html(html_string):
    data_stack = []
    root = None
    node = None

    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9]+)(.*?)>')
    for match in re.finditer(tag_pattern, html_string):
        tag, attributes = match.group(1), match.group(2)
        attributes = dict(re.findall(r'\s*([a-zA-Z0-9_-]+)\s*=\s*["\'](.*?)["\']', attributes))

        node_new = Node(tag, attributes=attributes)

        if not root:
            root = node_new
        else:
            node.children.append(node_new)
            node_new.parent = node

        if not re.search(r'/\s*>$', match.group(0)):
            data_stack.append(node)
            node = node_new

    text_pattern = re.compile(r'>([^<]*)<')
    for match in re.finditer(text_pattern, html_string):
        text = match.group(1).strip()

        if text and node:
            text_node = Node('#text', parent=node, text=text)
            node.children.append(text_node)

    def print_node(node, indent=0):
        print(node.__str__(indent))

        for child in node.children:
            print_node(child, indent + 1)

    return print_node(root)


class Node:
    def __init__(self, tag: str, parent=None, attributes=None, text=''):
        self.tag = tag
        self.parent = parent
        self.attributes = attributes if attributes else {}
        self.text = text
        self.children = []

    def __str__(self, indent=0):
        attributes_str = ', '.join(f'{key}: "{value}"' for key, value in self.attributes.items() if value)
        indent_str = '  ' * indent
        text_str = f', text="{self.text}"' if self.text else ''
        return (f'{indent_str}Node(tag={self.tag}'
                f'{", attributes={" + attributes_str + "}" if attributes_str else ""}{text_str})')

    def __repr__(self):
        children_repr = [child.tag if isinstance(child, Node) else repr(child) for child in self.children]
        return f'<Node object; tag={self.tag}, attributes={self.attributes}, children={children_repr}>'


index = '''
<html>
  <body bgcolor="red">
    <h1 id="first-header">My First Heading</h1>
    <p topmargin="12">My first paragraph.</p>
  </body>
</html>'''

root = parse_html(index)
print(str(root))
print(repr(root))
