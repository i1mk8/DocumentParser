from typing import Optional, List

import pytesseract
from lxml import etree
from lxml.etree import _Element

from DocumentParser.domain.IDocumentParser import IDocumentParser
from DocumentParser.domain.ValueObjects.BoundingBox import BoundingBox
from DocumentParser.domain.ValueObjects.line import Line
from DocumentParser.domain.ValueObjects.word import Word
from DocumentParser.domain.entities.block import Block
from DocumentParser.domain.entities.document import Document
from DocumentParser.domain.entities.page import Page


class ImageParser(IDocumentParser):
    _LXML_NAMESPACE = {'alto': 'http://www.loc.gov/standards/alto/ns-v3#'}

    def __init__(self, tesseract_path: Optional[str] = None):
        if tesseract_path is not None:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def process(self, path: str) -> Document:
        xml_ocr = pytesseract.image_to_alto_xml(path, lang='rus')
        root = etree.fromstring(xml_ocr)

        block_elements = root.findall('.//alto:TextBlock', namespaces=self._LXML_NAMESPACE)
        parsed_blocks = [self._parse_block(block) for block in block_elements]

        page = Page(blocks=parsed_blocks)

        return Document(
            path=path,
            source_type='image',
            pages=[page]
        )

    def _parse_block(self, block_element: _Element) -> Block:
        line_elements = block_element.findall('.//alto:TextLine', namespaces=self._LXML_NAMESPACE)
        parsed_lines = [self._parse_line(line) for line in line_elements]
        return Block(lines=parsed_lines)

    def _parse_line(self, line_element: _Element) -> Line:
        word_elements = line_element.findall('.//alto:String', namespaces=self._LXML_NAMESPACE)
        parsed_words = [self._parse_word(word) for word in word_elements]
        return Line(words=parsed_words)

    def _parse_word(self, word_element: _Element) -> Word:
        text = word_element.get('CONTENT')
        left = float(word_element.get('HPOS'))
        top = float(word_element.get('VPOS'))
        width = float(word_element.get('WIDTH'))
        height = float(word_element.get('HEIGHT'))

        bounding_box = BoundingBox(
            left=left,
            top=top,
            right=left + width,
            bottom=top + height
        )

        return Word(word=text, bounding_box=bounding_box)