# coding: utf-8
from markdown import markdown
import json

Dependencies = ['user']

class Parser:

    def __init__(self, raw, request, **kw):
        self.raw = raw
        self.request = request

    def format(self, formatter):
        output_html = markdown(
            self.raw,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.toc',
                'markdown.extensions.codehilite',
                ])
        try:
            self.request.write(formatter.rawHTML(output_html))
        except:
            self.request.write(formatter.escapedText(output_html))
