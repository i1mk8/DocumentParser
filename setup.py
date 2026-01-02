from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as file:
    required = file.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='document-parser',
    version='1.1.0',
    author='Aksenov Mikhail',

    description='Пакет для разбивки различных документов (docx, pdf, изображения) на страницы, блоки, строки и слова',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/i1mk8/DocumentParser',
    packages=find_packages(include=['document_parser', 'document_parser.*']),
    install_requires=required
)
