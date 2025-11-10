from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='document-parser',
    version='1.0.0',
    author='Aksenov Mikhail',

    description='Пакет для разбивки различных документов (docx, pdf, изображения) на страницы, блоки, строки и слова',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/i1mk8/DocumentParser',
    packages=find_packages(include=['DocumentParser', 'DocumentParser.*']),
    install_requires=required
)
