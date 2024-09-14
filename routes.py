from fastapi import FastAPI, Query
from typing import List, Optional
from .database import get_opensearch_client

app = FastAPI()

@app.get("/recipes/search/")
async def search_recipes(
    query: str,
    ingredients: Optional[List[str]] = Query(None),
    cuisine: Optional[str] = None,
    prep_time: Optional[int] = None,
    page: int = 1,
    size: int = 10
):
    client = get_opensearch_client()
    
    try:    
        search_query = {
            "from": (page - 1) * size,
            "size": size,
            "query": {
                "bool": {
                    "must": [{"match": {"recipe_name": query}}],
                    "filter": []
                }
            }
        }

        # Add filters for ingredients, cuisine, and prep_time if provided
        if ingredients:
            search_query['query']['bool']['filter'].append({
                "terms": {"ingredients": ingredients}
            })
        if cuisine:
            search_query['query']['bool']['filter'].append({
                "term": {"cuisine": cuisine}
            })
        if prep_time:
            search_query['query']['bool']['filter'].append({
                "range": {"prep_time": {"lte": prep_time}}
            })

        response = client.search(index="recipes", body=search_query)
        return response["hits"]["hits"]

    except Exception as e:
        return {"error": str(e)}