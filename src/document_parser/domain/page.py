from pydantic import BaseModel
from typing import List

from domain.block import Block


class Page(BaseModel):
    blocks: List[Block]
