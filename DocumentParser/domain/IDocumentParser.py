from abc import ABC, abstractmethod

from DocumentParser.domain.entities.document import Document


class IDocumentParser(ABC):
    @abstractmethod
    def process(self, path: str) -> Document:
        pass
