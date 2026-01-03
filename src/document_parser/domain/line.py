from pydantic import BaseModel
from typing import List

from domain.word import Word


class Line(BaseModel):
    """Строка текста обработанного документа."""

    words: List[Word]
