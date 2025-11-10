# Document Parser

Пакет для разбивки документов на страницы, блоки, строки и слова.

Поддерживаемые форматы документов:
* DOCX
* PDF
* PNG, JPG, JPEG, TIFF, BMP, GIF
## Установка
`pip install git+https://github.com/i1mk8/DocumentParser.git`
## Использование
```
>>> from DocumentParser import DocumentParser

>>> # Необходимо указывать при обработке изображений, если tesseract не добавлен в PATH
>>> TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract'

>>> document_parser = DocumentParser(TESSERACT_PATH)
>>> result = document_parser.parse('image.png')

>>> result
Document(
    path='image.png',
    source_type='image',
    pages=[Page(
        blocks=[Block(
            lines=[Line(
                words=[Word(
                word='Пример',
                bounding_box=BoundingBox(left=28.3, top=32.0, right=36.1, bottom=33.2))]
            )]
        )]
    )]
)
```
## Примеры
Примеры работы с разными типами документов:
* [DOCX](examples/docx)
* [PDF](examples/pdf)
* [Изображение (PNG)](examples/image)
