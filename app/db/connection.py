import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from ..core import settings

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(settings.DATABASE_URL, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

# Dependencia para FastAPI
def get_db():
    with get_db_connection() as cursor:
        yield cursor        