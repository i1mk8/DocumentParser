from pydantic import BaseModel
from typing import List

from document_parser.domain.value_objects.line import Line


class Block(BaseModel):
    lines: List[Line]
