from datetime import datetime
from backend.services.newsapi import get_articles
from elastic.es_client import es, INDEX_NAME

def index_articles():
    articles = get_articles()["articles"]

    for article in articles:
        doc = {
            "title":article["title"],
            "url":article["url"],
            "publised":article["publishedAt"],
            "timestamp":datetime.now(),
        }
        es.index(index=INDEX_NAME, body=doc)

    return {"message":"Ariticle indexed", "count": len(articles)}