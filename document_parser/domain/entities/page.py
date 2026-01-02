from pydantic import BaseModel
from typing import List

from document_parser.domain.entities.block import Block


class Page(BaseModel):
    blocks: List[Block]
