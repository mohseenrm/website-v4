import os
from re import sub
from stringcase import spinalcase
# Paths
dirname = os.path.dirname(__file__)
markdown_path = os.path.join(dirname, '../website/content/book')

def kebab(s):
    return sub(
        r"(\s|_|-|:|#|,|\(|\))+", "-",
            sub(
                r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                lambda mo: mo.group(0).lower(), s))

def write_book_to_md(book):
    print(book['title'])
    title = kebab(book['title'])
    print(f'title: {title}')

    # with open(f'{markdown_path}/')
