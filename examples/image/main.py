from DocumentParser import DocumentParser

# Необходимо указывать при обработке изображений, если tesseract не добавлен в PATH
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract'

document_parser = DocumentParser(TESSERACT_PATH)
result = document_parser.parse('image.png')

print(result)
with open('result.json', 'w', encoding='utf-8') as file:
    file.write(result.to_json(indent=4))
