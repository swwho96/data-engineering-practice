import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')


def get_articles():
    url = ('https://newsapi.org/v2/top-headlines?'
        'q=GPT&'
        # 'country=us&'
        'sortBy=publishedAt&'
        f'apiKey={API_KEY}')

    response = requests.get(url)
    return response.json()