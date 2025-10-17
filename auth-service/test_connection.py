import os
import psycopg2
import redis

POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

print("🔍 Probando conexión a PostgreSQL...")
try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="localhost",
        port=5432
    )
    print("✅ Conectado correctamente a PostgreSQL")
except Exception as e:
    print("❌ Error en PostgreSQL:", e)

print("\n🔍 Probando conexión a Redis...")
try:
    r = redis.Redis(host="localhost", port=6379)
    r.ping()
    print("✅ Conectado correctamente a Redis")
except Exception as e:
    print("❌ Error en Redis:", e)
