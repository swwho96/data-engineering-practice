from fastapi import FastAPI
import uvicorn
from backend.services.newsapi import get_articles
from elastic.article_to_es import index_articles
from elastic.es_client import es, INDEX_NAME

app = FastAPI()

@app.get('/')
def read_root():
    return {"meassage": "최신 AI 뉴스 모아보기"}

@app.get('/articles')
def articles_api():
    articles = get_articles()
    return {"articles": articles}


@app.get('/index_articles')
def indexing_articles():
    return index_articles()



@app.get('/search')
def search_articles(key:str):
    query = {
        "query": {
            "match": {
                "title": key
            }
        }
    }
    result = es.search(index=INDEX_NAME, body=query)
    return {"result":result["hits"]["hits"]}


if __name__ == "__main__":
    uvicorn.run("news_main:app", host="0.0.0.0", port=8000, reload=True)