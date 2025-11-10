from pydantic import BaseModel
from typing import List

from DocumentParser.domain.ValueObjects.word import Word


class Line(BaseModel):
    words: List[Word]
