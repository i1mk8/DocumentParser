from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_ALIGN_PARAGRAPH
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from DocumentParser.infrastructure.DocxParser.DocxParserConstants import *
from DocumentParser.infrastructure.DocxParser import DocxParerUtils
from DocumentParser.domain.entities.block import Block

from typing import List, Tuple


def get_page_size(document: Document) -> Tuple[float, float]:
    if document.sections:
        page_width = document.sections[0].page_width
        page_height = document.sections[0].page_height

        if document.sections and page_width and page_height:
            return DocxParerUtils.twip_to_point(page_width), DocxParerUtils.twip_to_point(page_height)

    return DEFAULT_PAGE_WIDTH_PT, DEFAULT_PAGE_HEIGHT_PT


# TODO: Отказаться от dict в пользу собственной структуры данных
def get_page_margins(document: Document) -> dict:
    margins = {
        'top': DEFAULT_MARGIN_TOP_PT,
        'right': DEFAULT_MARGIN_RIGHT_PT,
        'bottom': DEFAULT_MARGIN_BOTTOM_PT,
        'left': DEFAULT_MARGIN_LEFT_PT,
    }

    if document.sections:
        section = document.sections[0]
        if section.top_margin:
            margins['top'] = section.top_margin.pt
        if section.right_margin:
            margins['right'] = section.right_margin.pt
        if section.bottom_margin:
            margins['bottom'] = section.bottom_margin.pt
        if section.left_margin:
            margins['left'] = section.left_margin.pt

    return margins


def get_font_size(run: Run) -> float:
    if run.font.size and run.font.size.pt:
        return run.font.size.pt

    if run.style and run.style.font and run.style.font.size:
        return run.style.font.size.pt

    return DEFAULT_FONT_SIZE_PT


def get_word_width(word: str, font_size: float, is_bold: bool) -> float:
    avg_char_width = font_size * CHAR_WIDTH_FACTOR

    if is_bold:
        avg_char_width *= BOLD_FONT_FACTOR

    return len(word) * avg_char_width


# TODO: Отказаться от Tuple в пользу собственной структуры данных
def get_line_height(words: List[Tuple]) -> float:
    if not words:
        return EMPTY_LINE_SPACING_PT

    max_font_size = max(word[1] for word in words)
    return max_font_size * LINE_HEIGHT_FACTOR


def get_line_start_x(
        alignment: WD_PARAGRAPH_ALIGNMENT,
        left_offset: float,
        available_width: float,
        total_width: float
) -> float:
    if alignment == WD_ALIGN_PARAGRAPH.CENTER:
        return left_offset + (available_width - total_width) / 2
    elif alignment == WD_ALIGN_PARAGRAPH.RIGHT:
        return left_offset + available_width - total_width
    else:
        return left_offset


def get_left_paragraph_indent(paragraph: Paragraph) -> float:
    if paragraph.paragraph_format.left_indent is not None:
        return paragraph.paragraph_format.left_indent.pt
    return 0


def get_right_paragraph_indent(paragraph: Paragraph) -> float:
    if paragraph.paragraph_format.right_indent is not None:
        return paragraph.paragraph_format.right_indent.pt
    return 0


def get_paragraph_height(block: Block, start_y: float) -> float:
    if not block.lines:
        return start_y + EMPTY_LINE_SPACING_PT

    max_bottom = start_y
    for line in block.lines:
        for word in line.words:
            max_bottom = max(max_bottom, word.bounding_box.bottom)

    return max_bottom + PARAGRAPH_SPACING_PT
