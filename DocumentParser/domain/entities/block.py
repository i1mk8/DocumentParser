from pydantic import BaseModel
from typing import List

from DocumentParser.domain.ValueObjects.line import Line


class Block(BaseModel):
    lines: List[Line]
