from opensearchpy import OpenSearch

# Function to get OpenSearch client
def get_opensearch_client():
    client = OpenSearch(
        hosts=[{'host': 'localhost', 'port': 9200}],
        http_auth=('admin', 'admin'),
        use_ssl=False,  # Do not use SSL if OpenSearch is running on HTTP
        verify_certs=False  # This option becomes irrelevant if SSL is off
    )
    return client


# Test the connection to OpenSearch
def test_connection():
    client = get_opensearch_client()
    info = client.info()  # Fetch cluster info
    print(info)

if __name__ == "__main__":
    test_connection()
