from pydantic import BaseModel
from typing import List

from domain.word import Word


class Line(BaseModel):
    words: List[Word]
