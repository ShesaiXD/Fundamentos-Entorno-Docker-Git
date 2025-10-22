import os
import psycopg2
import redis

# Variables de entorno
pg_user = os.getenv("POSTGRES_USER", "postgres")
pg_pass = os.getenv("POSTGRES_PASSWORD", "12345")
pg_db   = os.getenv("POSTGRES_DB", "postgres")
pg_host = "localhost"
pg_port = 5433

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

try:
    conn = psycopg2.connect(
        user=pg_user,
        password=pg_pass,
        dbname=pg_db,
        host=pg_host,
        port=pg_port
    )
    print("✅ Conexión a PostgreSQL exitosa!")
    conn.close()
except Exception as e:
    print("❌ Error conectando a PostgreSQL:", e)

try:
    r = redis.Redis(host=redis_host, port=redis_port)
    r.ping()
    print("✅ Conexión a Redis exitosa!")
except Exception as e:
    print("❌ Error conectando a Redis:", e)
