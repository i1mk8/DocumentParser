from abc import ABC, abstractmethod

from document_parser.domain.entities.document import Document


class BaseDocumentParser(ABC):
    @abstractmethod
    def process(self, path: str) -> Document:
        pass
