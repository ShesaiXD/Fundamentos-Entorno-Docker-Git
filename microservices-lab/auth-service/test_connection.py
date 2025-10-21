# auth-service/test_connection.py
import os
import sys
import time

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def test_postgres():
    try:
        import psycopg2
    except Exception as e:
        print("psycopg2 no encontrado:", e)
        return False

    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            port=POSTGRES_PORT,
            connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        print("Postgres OK — SELECT 1 ->", result)
        return True
    except Exception as e:
        print("Error conectando a Postgres:", e)
        return False

def test_redis():
    try:
        import redis
    except Exception as e:
        print("redis lib no encontrada:", e)
        return False

    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=5)
        pong = r.ping()
        print("Redis OK — PING ->", pong)
        return True
    except Exception as e:
        print("Error conectando a Redis:", e)
        return False

if __name__ == "__main__":
    print("Lectura variables de entorno:")
    print("POSTGRES_HOST=", POSTGRES_HOST)
    print("POSTGRES_USER=", POSTGRES_USER)
    print("POSTGRES_DB=", POSTGRES_DB)
    print("REDIS_HOST=", REDIS_HOST)
    print("REDIS_PORT=", REDIS_PORT)
    time.sleep(1)

    ok_pg = test_postgres()
    ok_redis = test_redis()
    if ok_pg and ok_redis:
        print("Conexiones OK ✅")
        sys.exit(0)
    else:
        print("Al menos una conexión falló ❌")
        sys.exit(1)