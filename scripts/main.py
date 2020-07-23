from goodreads import Goodreads
from markdown_writer import write_book_to_md


if __name__ == "__main__":
    books = Goodreads().retreive_books_from_shelf()
    # print(books)
    for book in books:
        write_book_to_md(book)
