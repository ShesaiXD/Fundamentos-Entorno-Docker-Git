from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# Variables de entorno
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

@app.route("/ping")
def ping():
    """Verifica conexión con Postgres y Redis"""
    status = {"postgres": False, "redis": False}

    # PostgreSQL
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
        cur.fetchone()
        cur.close()
        conn.close()
        status["postgres"] = True
    except Exception as e:
        status["postgres"] = f"Error: {e}"

    # Redis
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=5)
        pong = r.ping()
        status["redis"] = pong
    except Exception as e:
        status["redis"] = f"Error: {e}"

    return jsonify(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)