from pydantic import BaseModel
from typing import List

from DocumentParser.domain.entities.block import Block


class Page(BaseModel):
    blocks: List[Block]
