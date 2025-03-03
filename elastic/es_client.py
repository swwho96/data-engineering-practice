import subprocess
from elasticsearch import Elasticsearch

# subprocess.Popen([
#     "elasticsearch",
#     "-E", "path.data=C:/Users/swwho/Desktop/ainews/data/"
# ])
es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "new_articles"

def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body={
            "settings":{"number_of_shards":1},
            "mappings":{
                "properties": {
                    "title": {"type":"text"},
                    "url": {"type":"keyword"},
                    "publised": {"type":"date"},
                    "timestamp":{"type":"date"},
                }
            }
        })