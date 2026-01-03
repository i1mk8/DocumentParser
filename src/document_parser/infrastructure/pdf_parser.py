from typing import List
from collections import defaultdict

import fitz

from document_parser.domain.base_document_parser import BaseDocumentParser
from domain.page import Page
from domain.block import Block
from domain.document import Document
from domain.line import Line
from domain.word import Word
from domain.bounding_box import BoundingBox


class PdfParser(BaseDocumentParser):
    """Парсер pdf документов."""

    _SUPPORTED_EXTENSIONS = ['.pdf']

    @property
    def supported_extensions(self) -> List[str]:
        return self._SUPPORTED_EXTENSIONS

    def process(self, path: str) -> Document:
        with fitz.open(path) as file:
            parsed_pages = []

            for page in file:
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
