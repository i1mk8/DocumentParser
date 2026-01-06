from pydantic import BaseModel
from typing import List, Dict

from document_parser.domain.page import Page


class Document(BaseModel):
    """Обработанный документ."""

    path: str
    source_type: str

    pages: List[Page]

    def to_json(self, **kwargs) -> str:
        """
         Сериализует документ в JSON строку.

        :param kwargs: Аргументы, передаваемые в model_dump_json (например, indent=4 для отступов)
        :return: Строка JSON
        """
        return self.model_dump_json(**kwargs)

    def to_dict(self, **kwargs) -> Dict:
        """
        Преобразует документ в словарь.

        :param kwargs: Аргументы, передаваемые в model_dump
        :return: Словарь
        """
        return self.model_dump(**kwargs)
