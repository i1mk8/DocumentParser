from DocumentParser.domain.IDocumentParser import IDocumentParser
from typing import List
from collections import defaultdict

from DocumentParser.domain.entities.page import Page
from DocumentParser.domain.entities.block import Block
from DocumentParser.domain.entities.document import Document
from DocumentParser.domain.ValueObjects.line import Line
from DocumentParser.domain.ValueObjects.word import Word
from DocumentParser.domain.ValueObjects.BoundingBox import BoundingBox

import fitz


class PdfParser(IDocumentParser):
    def process(self, path: str) -> Document:
        pdf_document = fitz.open(path)
        parsed_pages = []

        for page in pdf_document:
            page_blocks = self._parse_page_words(page)
            parsed_pages.append(Page(blocks=page_blocks))

        return Document(
            path=path,
            source_type='pdf',
            pages=parsed_pages
        )

    def _parse_page_words(self, page: fitz.Page) -> List[Block]:
        words = page.get_text('words')
        blocks_dict = defaultdict(lambda: defaultdict(list))

        for word in words:
            left, top, right, bottom, text, block_index, line_index, _ = word

            bounding_box = BoundingBox(
                left=left,
                top=top,
                right=right,
                bottom=bottom,
            )
            blocks_dict[block_index][line_index].append(Word(word=text, bounding_box=bounding_box))

        parsed_blocks = []
        for block_index in sorted(blocks_dict.keys()):
            parsed_lines = []

            for line_index in sorted(blocks_dict[block_index].keys()):
                words_list = blocks_dict[block_index][line_index]
                parsed_lines.append(Line(words=words_list))

            parsed_blocks.append(Block(lines=parsed_lines))
        return parsed_blocks
