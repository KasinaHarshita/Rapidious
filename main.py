from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from opensearchpy import OpenSearch
from app.postgres_db import get_postgres_connection
from app.database import get_opensearch_client

app = FastAPI()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: str
    cuisine: str
    prep_time: int

def insert_recipe_into_postgres(recipe_name, ingredients, cuisine, prep_time):
    conn = get_postgres_connection()
    cursor = conn.cursor()
    query = """INSERT INTO recipes (recipe_name, ingredients, cuisine, prep_time) 
               VALUES (%s, %s, %s, %s) RETURNING id;"""
    cursor.execute(query, (recipe_name, ingredients, cuisine, prep_time))
    recipe_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return recipe_id

def index_recipe_in_opensearch(recipe_id, recipe_name, ingredients, cuisine, prep_time):
    client = get_opensearch_client()
    document = {
        "id": recipe_id,
        "recipe_name": recipe_name,
        "ingredients": ingredients,
        "cuisine": cuisine,
        "prep_time": prep_time
    }
    client.index(index="recipes", id=recipe_id, body=document)

@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    # Step 1: Insert the recipe into PostgreSQL
    recipe_id = insert_recipe_into_postgres(
        recipe.recipe_name, recipe.ingredients, recipe.cuisine, recipe.prep_time
    )
    
    # Step 2: Index the recipe in OpenSearch for searching
    index_recipe_in_opensearch(
        recipe_id, recipe.recipe_name, recipe.ingredients, recipe.cuisine, recipe.prep_time
    )

    return {"message": "Recipe created successfully", "recipe_id": recipe_id}


    