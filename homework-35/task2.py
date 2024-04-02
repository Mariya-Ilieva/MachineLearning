from abc import ABC, abstractmethod
import re


class SaxParser(ABC):
    def tag_info(self, tag):
        tag_match = re.match(r'([a-zA-Z]+)(.*)', tag)
        tag_name, attrs_str = tag_match.groups()

        attrs = dict(re.findall(r'([a-zA-Z]+)="([^"]*)"', attrs_str))

        return tag_name, attrs

    def parse(self, html):
        pattern = r'<(/?[a-zA-Z]+).*?>|([^<]+)'
        matches = re.finditer(pattern, html)

        for match in matches:
            tag, text = match.groups()

            if tag:
                if tag.startswith('/'):
                    self.end_tag(tag[1:])
                else:
                    tag_name, attrs = self.tag_info(tag)
                    self.start_tag(tag_name, attrs)

            elif text:
                self.data(text)


    @abstractmethod
    def start_tag(self, tag, attrs):
        pass

    @abstractmethod
    def end_tag(self, tag):
        pass

    @abstractmethod
    def data(self, text):
        pass


class TestParser(SaxParser):
    def start_tag(self, tag, attrs):
        print(f'start tag: {tag}, attrs: {attrs}')

    def end_tag(self, tag):
        print(f'end tag: {tag}')

    def data(self, text):
        print(f'text: {text}')


html = '''
<html>
  <head><title>Test page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>Hello <b>Ivan</b>. How are you?<p>
  </body>
</html>
'''

parser = TestParser()
parser.parse(html)
