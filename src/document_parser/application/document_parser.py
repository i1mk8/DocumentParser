from typing import Optional
import os

from document_parser.application.document_parser_exceptions import UnsupportedFileError
from domain.document import Document
from document_parser.infrastructure.image_parser import ImageParser
from document_parser.infrastructure.pdf_parser import PdfParser
from document_parser.infrastructure.docx_parser import DocxParser


class DocumentParser:
    """
    Класс для разбивки документов на страницы, блоки, строки и слова.
    Поддерживаемые форматы документов: docx, pdf, png, jpg, jpeg, tiff, bmp, gif
    """

    def __init__(self, tesseract_path: Optional[str]=None, libre_office_path: Optional[str]=None, ocr_lang: str='rus'):
        """
        :param tesseract_path: Путь к Tesseract
        :param libre_office_path: Путь к LibreOffice
        :param ocr_lang: Язык Tesseract OCR
        """
        pdf_parser = PdfParser()
        self._parsers = [
            pdf_parser,
            ImageParser(ocr_lang, tesseract_path),
            DocxParser(pdf_parser, libre_office_path)
        ]

    def parse(self, path: str) -> Document:
        """
        Разбивает документ на страницы, блоки, строки и слова.

        :param path: Путь к файлу, который будет обработан
        :return: Обработанный файл
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f'Путь {path} не существует')

        _, extension = os.path.splitext(path.lower())
        for parser in self._parsers:
            if extension in parser.supported_extensions:
                return parser.process(path)

        raise UnsupportedFileError(f'Файл {path} с расширением {extension} не поддерживается')
