import re


def get_node(html_tag):
    match = re.search(r'<([a-zA-Z]+)\s*([^>]*)>', html_tag)

    if match:
        tag_name = match.group(1)
        attributes_str = match.group(2)

        attributes = {}

        matches = re.findall(r'\s*([a-zA-Z_][a-zA-Z0-9_-]*)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', attributes_str)
        for a in matches:
            attr_name = a[0]
            attr_value = a[1] or a[2]
            attributes[attr_name] = attr_value

        return Node(tag=tag_name, attributes=attributes)
    else:
        return None


class Node:
    def __init__(self, tag: str, attributes: dict):
        self.tag = tag
        self.attributes = attributes


s = "<a href='#section1' class='header' id='12'>"
n = get_node(s)
print(f'tag={n.tag}, attributes={n.attributes}')
