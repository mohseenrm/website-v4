import logging
import os
from datetime import datetime
from re import sub
from stringcase import spinalcase
# Paths
dirname = os.path.dirname(__file__)
markdown_path = os.path.join(dirname, '..', 'website', 'content', 'book')


def markdown_file_content(book):
    return """---
title: "{readable_title}"
date: {date}
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
goodreads: "{goodreads_link}"
image: "{image}"
---
""".format(**book)

def kebab(value):
    transformed_string = sub(r'[^0-9a-zA-Z]+', '-', value)
    if (transformed_string[-1] != '-'):
        return transformed_string
    return transformed_string[:-1]

def write_book_to_md(book):
    title = kebab(book['title'])

    book['title'] = title
    book['readable_title'] = title.replace('-', ' ')
    book['date'] = datetime.utcnow()

    file_path = f'{markdown_path}/{title}.md'
    logging.info(f'Writing file: {file_path}')

    with open(file_path, 'w+') as markdown:
        markdown.write(markdown_file_content(book))
        logging.info('Write complete!')

