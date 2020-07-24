import json
import logging
import os
import requests
import xmltodict


class Goodreads:
    _user_id = '40671307'
    _to_read_shelf_id = '132439173'

    def __init__(self):
        self.api_key = os.environ['GOODREADS_KEY']
        self.api_secret = os.environ['GOODREADS_SECRET']

    def retreive_books_from_shelf(self):
        assert self.api_key is not None

        to_read_books = []

        params = {
            'key': self.api_key,
            'user_id': self._user_id,
            'shelf': 'to-read',
            'sort': 'date_added',
            # Descending
            'order': 'd',
            # API version
            'v': 2
        }
        logging.info('Fetching books from shelf')

        url = f'https://www.goodreads.com/review/list/{self._user_id}'
        response = requests.get(url, params)
        book_shelf = xmltodict.parse(response.content)

        logging.info('Parsing results...')
        books = book_shelf.get('GoodreadsResponse',
                               {}).get('reviews', {}).get('review', [])

        for book_data in books:
            book = book_data['book']

            to_read_books.append({
                'title': book['title'],
                'goodreads_link': book['link'],
                'image': book['image_url'],
            })

        return to_read_books
