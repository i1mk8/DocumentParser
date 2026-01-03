from pydantic import BaseModel

from domain.bounding_box import BoundingBox


class Word(BaseModel):
    word: str
    bounding_box: BoundingBox
