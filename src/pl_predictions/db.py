import os 
import psycopg

from dotenv import load_dotenv

load_dotenv()

def connect():
    return psycopg.connect(
        host=os.environ["PGHOST"],
        port=os.environ["PGPORT"],
        user=os.environ["PGUSER"],
        password=os.environ["PGPASSWORD"],
        dbname=os.environ["PGDATABASE"],
        sslmode=os.getenv("PGSSLMODE","require"),
    )
