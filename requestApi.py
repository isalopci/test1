import re
import requests

class requestApi:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.title = self.formatString(title) if title else title 
        self.author = self.formatString(author) if author else author

    def formatString(self, name:str) -> str:
        return re.sub(r'\s+','%20',name)
        
    def buildUrl(self) -> str:

        base_url = 'http://openlibrary.org/search.json'

        if self.author:
            query = f'?author={self.author}'
        elif self.title:
            query = f'?title={self.title}'
        
        return base_url + query
    
     # Fetch cover image with default size L when not given
    @staticmethod
    def fetchCoverImage(id:str, size:str = 'L') -> str:
        if size not in ['S','M','L']:
            raise Exception('An image size must be entered (S, M or L)')
        return f'https://covers.openlibrary.org/b/id/{id}-{size}.jpg'


    def fetchBooks(self):
        url = self.buildUrl()
        response = requests.get(url)
        return response.json()

