from pydantic import BaseModel


class BoundingBox(BaseModel):
    left: float
    top: float
    right: float
    bottom: float
