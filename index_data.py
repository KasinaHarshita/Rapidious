from opensearchpy import OpenSearch
import pandas as pd
from opensearchpy.helpers import bulk

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
)

mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "ingredients": {"type": "text"},
            "cuisine": {"type": "keyword"},
            "prep_time": {"type": "integer"},
            "cook_time": {"type": "integer"},
            "total_time": {"type": "integer"},
            "rating": {"type": "float"}
        }
    }
}

client.indices.create(index="epirecipes", body=mapping)

data = pd.read_csv("C:/Users/harsh/rapidious_backend/epi_r.csv")

def format_data(row):
    return {
        "title": row["title"],
        "ingredients": row["ingredients"],
        "cuisine": row["cuisine"],
        "prep_time": int(row["prep_time"]),
        "cook_time": int(row["cook_time"]),
        "total_time": int(row["total_time"]) + int(row["cook_time"]),
        "rating": int(row["rating"]),
    }

documents = [format_data(row) for _, row in data.iterrows()]

actions = [
    {
        "index": "epirecipes",
        "_source": document
    }
    for document in documents
]
bulk(client, actions)

response = client.search(index="epirecipes", body={"query": {"match_all": {}}})
print(response)