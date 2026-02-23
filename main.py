import os
import psycopg
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    try:
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            return {"db": "error", "details": "DATABASE_URL is None"}

        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()

        return {"db": "connected", "result": result[0]}

    except Exception as e:
        return {"db": "error", "details": str(e)}
