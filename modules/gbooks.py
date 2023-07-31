"""
Google Books API

This module provides functionality for App Users.
"""

# pylint: disable=E0401
from flask_restx import Namespace, Resource, fields

import requests

api = Namespace("books", description="Google Book related operations")

@api.route('/<string:query>')
@api.param("query", "The search query")
@api.response(404, "No Books Found")
class BookSearch(Resource):
    def get(self, query):
        # Make a request to the Google Books API
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}', timeout=10)

        if response.status_code == 200:
            # Parse the response and extract relevant book information
            data = response.json()
            books = []

            if 'items' in data:
                for item in data['items']:
                    volumeInfo = item['volumeInfo']
                    book_info = {   
                        'title': volumeInfo.get('title', 'N/A'),
                        'author': volumeInfo.get('authors', ['N/A']),
                        'main_category': volumeInfo.get('mainCategory', 'N/A'),
                        'categories': volumeInfo.get('categories', 'N/A'),
                        'published_date': volumeInfo.get('publishedDate', 'NA'),
                        'average_rating': volumeInfo.get('averageRating', 'N/A'),
                        'rating_count': volumeInfo.get('ratingsCount', 'N/A'),
                        'description': volumeInfo.get('description', 'N/A'),
                        'thumbnail': volumeInfo.get('imageLinks', {}).get('thumbnail', 'N/A'),
                        'page_count': volumeInfo.get('pageCount', 'N/A'),
                        'retail_price': volumeInfo.get('saleInfo', {}).get('retailPrice', 'N/A'),
                        'list_price': volumeInfo.get('saleInfo', {}).get('listPrice', 'N/A')
                    }
                    books.append(book_info)

            return {'books': books}
        else:
            return {'message': 'Error retrieving books'}, response.status_code
