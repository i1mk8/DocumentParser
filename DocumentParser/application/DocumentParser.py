from typing import Optional
import os

from DocumentParser.application.DocumentParserExceptions import UnsupportedFileError

from DocumentParser.domain.entities.document import Document

from DocumentParser.infrastructure.ImageParser.ImageParser import ImageParser
from DocumentParser.infrastructure.PdfParser.PdfParser import PdfParser
from DocumentParser.infrastructure.DocxParser.DocxParser import DocxParser


class DocumentParser:
    _IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
    _PDF_EXTENSIONS = ['.pdf']
    _DOCX_EXTENSIONS = ['.docx']

    _pdf_parser = PdfParser()
    _docx_parser = DocxParser()

    def __init__(self, tesseract_path: Optional[str]=None):
        self._image_parser = ImageParser(tesseract_path=tesseract_path)

    def parse(self, path: str) -> Document:
        if not os.path.exists(path):
            raise FileNotFoundError(f'Путь {path} не существует')

        _, extension = os.path.splitext(path.lower())

        if extension in self._IMAGE_EXTENSIONS:
            return self._image_parser.process(path)
        if extension in self._PDF_EXTENSIONS:
            return self._pdf_parser.process(path)
        if extension in self._DOCX_EXTENSIONS:
            return self._docx_parser.process(path)

        raise UnsupportedFileError(f'Файл {path} с расширением {extension} не поддерживается')
