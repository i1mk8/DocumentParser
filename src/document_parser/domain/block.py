from pydantic import BaseModel
from typing import List

from domain.line import Line


class Block(BaseModel):
    lines: List[Line]
