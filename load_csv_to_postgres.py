import pandas as pd
import psycopg2
from psycopg2 import sql

# Define your PostgreSQL connection details
def get_postgres_connection():
    return psycopg2.connect(
        dbname="recipes_db",
        user="postgres",
        password="Navya123$%^",
        host="localhost",
        port="5432"
    )

def load_csv_to_postgres(csv_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv("C:/Users/harsh/Fast_API_Application/app/epi_r.csv")

    # Establish a connection to PostgreSQL
    conn = get_postgres_connection()
    cursor = conn.cursor()

    # Define the SQL query for inserting data
    insert_query = sql.SQL("""
        INSERT INTO recipes (recipe_name, ingredients, cuisine, prep_time) 
        VALUES (%s, %s, %s, %s)
    """)

    # Iterate over DataFrame rows and insert each row into PostgreSQL
    for index, row in df.iterrows():
        cursor.execute(insert_query, (row['recipe_name'], row['ingredients'], row['cuisine'], row['prep_time']))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully.")

if __name__ == "__main__":
    # Provide the path to your CSV file here
    csv_file_path = 'path/to/your/recipes.csv'
    load_csv_to_postgres(csv_file_path)
