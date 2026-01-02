from pydantic import BaseModel
from typing import List

from document_parser.domain.value_objects.word import Word


class Line(BaseModel):
    words: List[Word]
