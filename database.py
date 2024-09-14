from opensearchpy import OpenSearch

def get_opensearch_client():
    client = OpenSearch(
        hosts=[{'host': 'localhost', 'port': 9200}],
        http_auth=('admin', 'admin'),
        use_ssl=True,
        verify_certs=False
    )
    return client

def create_recipes_index():
    client = get_opensearch_client()
    index_body = {
        "mappings": {
            "properties": {
                "recipe_name": {"type": "text"},
                "ingredients": {"type": "text"},
                "cuisine": {"type": "keyword"},
                "prep_time": {"type": "integer"}
            }
        }
    }
    response = client.indices.create(index="recipes", body=index_body)
    print(response)

if __name__ == "__main__":
    create_recipes_index()