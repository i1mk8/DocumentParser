from pydantic import BaseModel

from document_parser.domain.value_objects.bounding_box import BoundingBox


class Word(BaseModel):
    word: str
    bounding_box: BoundingBox
