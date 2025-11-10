from DocumentParser import DocumentParser

# Необходимо указывать при обработке изображений, если tesseract не добавлен в PATH
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract'

document_parser = DocumentParser(TESSERACT_PATH)
print(document_parser.parse('image.png'))
