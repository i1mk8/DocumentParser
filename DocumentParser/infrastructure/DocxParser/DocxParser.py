from typing import Optional

import os
import platform
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from DocumentParser.domain.IDocumentParser import IDocumentParser
from DocumentParser.domain.entities.document import Document

from DocumentParser.infrastructure.PdfParser.PdfParser import PdfParser


class DocxParser(IDocumentParser):
    _LIBRE_OFFICE_WINDOWS_PATH = r'C:\Program Files\LibreOffice\program\soffice.exe'

    _pdf_parser = PdfParser()

    def __init__(self, libre_office_path: Optional[str] = None):
        if libre_office_path is not None:
            self._libre_office_path = libre_office_path

        else:
            if platform.system() == 'Windows' and os.path.exists(self._LIBRE_OFFICE_WINDOWS_PATH):
                self._libre_office_path = self._LIBRE_OFFICE_WINDOWS_PATH
            else:
                self._libre_office_path = 'libreoffice'

    def process(self, path: str) -> Document:
        # TODO: Потенциальная коллизия имен при многопоточной работе
        with TemporaryDirectory() as temp_dir:
            pdf_path = self._docx2pdf(temp_dir, path)

            result = self._pdf_parser.process(pdf_path)
            result.path = path
            result.source_type = 'docx'

            return result

    def _docx2pdf(self, out_dir: str, docx_path) -> str:
        subprocess.run(
            [self._libre_office_path, '--headless', '--convert-to', 'pdf', '--outdir', out_dir, docx_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        docx_path = Path(docx_path)
        pdf_path = Path(os.path.join(out_dir, docx_path.name)).with_suffix('.pdf')
        return str(pdf_path)
