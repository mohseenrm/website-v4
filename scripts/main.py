import logging
from goodreads import Goodreads
from markdown_writer import write_book_to_md

logging.basicConfig(filename="output.log", level=logging.INFO)

if __name__ == "__main__":
    logging.info("/**********************START*************************/")
    books = Goodreads().retreive_books_from_shelf()

    for book in books:
        write_book_to_md(book)
    logging.info("/**********************COMPLETE*************************/")
