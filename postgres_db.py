import psycopg2

def get_postgres_connection():
    conn = psycopg2.connect(
        dbname="recipes_db",
        user="postgres",
        password="Navya123$%^",
        host="localhost",
        port="5432"
    )
    return conn
