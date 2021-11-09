from __future__ import annotations

from utils.stringutil import trim_margin
from typing import List


class Tag:
    children: List[Tag]

    def __init__(self, name, value=None, indent=0, parent=None):
        self.name = name
        self.value = value
        self.parent = parent
        self.indent = indent

    def add_child(self, tag_name) -> Tag:
        tag = Tag(tag_name, indent=self.indent + 1, parent=self)
        self.value = tag
        return tag

    def __str__(self):
        indent = '    ' * self.indent
        return trim_margin(f'''\
            |{indent}<{self.name}>
            |{indent}    {self.value}
            |{indent}</{self.name}>''')


class TagBuilder:
    def __init__(self, root_name='root'):
        self.root = Tag(root_name)
        self.tag = self.root

    def start_tag(self, tag_name):
        self.tag = self.tag.add_child(tag_name)
        return self.tag

    def set_value(self, value):
        self.tag.value = value

    def end_tag(self):
        tag = self.tag
        self.tag = tag.parent
        return tag

    def __str__(self):
        return str(self.tag)


builder = TagBuilder()
builder.start_tag('items')
builder.start_tag('gun')
builder.start_tag('name')
builder.set_value('m100')
builder.end_tag()
builder.end_tag()
builder.end_tag()

print(builder)
