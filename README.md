🧭 DÍA 2 — Ejercicio 2: BACKEND Microservicio Backend Auth (Django + DRF + JWT + PostgreSQL + Redis)
🎯 Objetivo general:
 Construir un microservicio de autenticación completamente independiente, que maneje usuarios, login y tokens JWT, corriendo en su propio contenedor Docker y conectado a PostgreSQL y Redis.

🧩 Conceptos clave
Autenticación basada en JWT (JSON Web Tokens)
Estructura de un servicio Django aislado
Configuración de variables de entorno y dependencias
Cacheo y sesiones con Redis
Comunicación segura entre servicios vía API


🕐 Video de referencia:
🎥 “Microservicios con Django REST Framework, Next.js y Apache Kafka”
 👉 https://www.youtube.com/watch?v=wj766sxHZrM
📍 Ver desde: minuto 26:13 hasta 2:54:00
(No ver ni implementar la parte de Kafka Producer — solo REST y Redis)

⚙️ Pasos del ejercicio
1️⃣ Crear el proyecto Django y app users
cd auth-service
django-admin startproject auth_service .
python manage.py startapp users

2️⃣ Configurar el Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]

3️⃣ Extender docker-compose.yml
auth:
  build: ./auth-service
  container_name: auth_service
  restart: always
  environment:
    - DEBUG=1
    - DB_HOST=postgres
    - DB_NAME=main_db
    - DB_USER=devuser
    - DB_PASS=devpass
    - REDIS_HOST=redis
    - REDIS_PORT=6379
  depends_on:
    - postgres
    - redis
  ports:
    - "8000:8000"


4️⃣ Instalar dependencias (en requirements.txt)
django==5.0
djangorestframework==3.15
djangorestframework-simplejwt==5.3
psycopg2-binary
redis
django-cors-headers


5️⃣ Configurar settings.py
Añadir rest_framework, corsheaders, users


Configurar DATABASES con variables de entorno


Configurar CACHES (Redis)


Añadir middleware corsheaders.middleware.CorsMiddleware


Definir REST_FRAMEWORK con JWTAuthentication



6️⃣ Modelo de usuario personalizado
En users/models.py:
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email obligatorio")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

Registrar en settings.py:
AUTH_USER_MODEL = 'users.User'


7️⃣ Endpoints con JWT
En users/views.py o rutas de API:
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

Configura rutas:
path('api/token/', TokenObtainPairView.as_view()),
path('api/token/refresh/', TokenRefreshView.as_view()),

Crea también un endpoint /api/register/ que permita crear usuarios.

8️⃣ Probar con Postman
POST /api/register/ → crea usuario


POST /api/token/ → genera access/refresh token


POST /api/token/refresh/ → renueva token


Verificar conexión con base de datos y Redis:
docker exec -it auth_service python manage.py shell


🧪 Reto adicional (opcional)
Implementar endpoint /api/me/ que devuelva la información del usuario autenticado.

📦 Entregables del Día 2
Entregable
Descripción
Código funcional del microservicio auth-service/
Proyecto Django con JWT, PostgreSQL y Redis
Dockerfile y docker-compose.yml actualizados
Contenedor funcionando en puerto 8000
Captura Postman
Evidencia de login, refresh y verify exitosos
README actualizado
Descripción del servicio y endpoints