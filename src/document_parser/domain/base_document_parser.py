from abc import ABC, abstractmethod
from typing import List

from domain.document import Document


class BaseDocumentParser(ABC):
    @property
    @abstractmethod
    def supported_extensions(self) -> List[str]:
        pass

    @abstractmethod
    def process(self, path: str) -> Document:
        pass
