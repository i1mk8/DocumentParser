from pydantic import BaseModel

from DocumentParser.domain.ValueObjects.BoundingBox import BoundingBox


class Word(BaseModel):
    word: str
    bounding_box: BoundingBox
