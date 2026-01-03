from pydantic import BaseModel
from typing import List

from domain.page import Page


class Document(BaseModel):
    path: str
    source_type: str

    pages: List[Page]

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)
