# 🧱 Proyecto: Microservicios con Docker Compose

## 🚀 Descripción del Proyecto

Este proyecto implementa una arquitectura basada en **microservicios** utilizando **Docker Compose**.
Incluye tres servicios principales:

* **Auth Service:** servicio de autenticación en Python/Flask.
* **Base de datos PostgreSQL:** almacena usuarios y datos persistentes.
* **Redis:** se utiliza como caché para mejorar el rendimiento.

Cada servicio está aislado y se comunica a través de una red interna creada por Docker.
El objetivo es demostrar la interoperabilidad entre servicios y la correcta configuración de un entorno desacoplado, modular y escalable.

---

## 🧩 Arquitectura General del Sistema

```
                  +-------------------------+
                  |       CLIENTE API        |
                  +-----------+--------------+
                              |
                              v
                  +-------------------------+
                  |     AUTH SERVICE         |
                  |   Flask / Python 3.11    |
                  +-----------+--------------+
                              |
             +----------------+----------------+
             |                                 |
             v                                 v
+-------------------------+       +-------------------------+
|     PostgreSQL DB       |       |        Redis Cache       |
|        (postgres:15)     |       |         (redis:7)        |
+-------------------------+       +-------------------------+
```

**Flujo principal:**

1. El cliente envía una solicitud HTTP al Auth Service.
2. El Auth Service valida la información y accede a la base de datos PostgreSQL.
3. Redis se utiliza como sistema de caché para mejorar la velocidad de respuesta.

---

## ⚙️ Estructura del Proyecto

```
microservices-lab/
│
├── auth-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── test_connection.py
│
├── docker-compose.yml
└── README.md
```

---

## 🐳 Configuración de los Servicios (docker-compose.yml)

```yaml
version: '3.8'

services:
  auth-service:
    build: ./auth-service
    container_name: auth-service
    ports:
      - "5000:5000"
    depends_on:
      - db
      - redis
    environment:
      - POSTGRES_HOST=db
      - POSTGRES_USER=devuser
      - POSTGRES_PASSWORD=devpass
      - POSTGRES_DB=main_db
      - REDIS_HOST=redis
    networks:
      - micro_net

  db:
    image: postgres:15
    container_name: db_postgres
    environment:
      - POSTGRES_USER=devuser
      - POSTGRES_PASSWORD=devpass
      - POSTGRES_DB=main_db
    ports:
      - "5432:5432"
    networks:
      - micro_net

  redis:
    image: redis:7
    container_name: cache_redis
    ports:
      - "6379:6379"
    networks:
      - micro_net

networks:
  micro_net:
    driver: bridge
```

---

## 🔧 Instrucciones de Ejecución

### 1️⃣ Construir y ejecutar los contenedores

```bash
docker compose up --build -d
```

### 2️⃣ Verificar los contenedores en ejecución

```bash
docker ps
```

Salida esperada:

```
CONTAINER ID   IMAGE         PORTS                  NAMES
xxxxx           redis:7       0.0.0.0:6379->6379/tcp  cache_redis
xxxxx           postgres:15   0.0.0.0:5432->5432/tcp  db_postgres
xxxxx           auth-service  0.0.0.0:5000->5000/tcp  auth-service
```

### 3️⃣ Probar la conexión entre servicios

```bash
docker exec -it auth-service python test_connection.py
```

---

## 🧠 Verificación de Conectividad

El script `test_connection.py` ejecuta pruebas automáticas para validar la conexión con **PostgreSQL** y **Redis**, mostrando mensajes de éxito o error en consola.

Ejemplo de salida:

```
Postgres OK — SELECT 1 -> (1,)
Redis OK — PING -> True
Conexiones OK ✅
```

---

## ✅ Checklist de Implementación

| Nº | Requisito                | Descripción                           | Estado |
| -- | ------------------------ | ------------------------------------- | ------ |
| 1  | **Dockerfile**           | Archivo configurado para Python/Flask | ✅      |
| 2  | **requirements.txt**     | Dependencias correctamente definidas  | ✅      |
| 3  | **docker-compose.yml**   | Configuración funcional de servicios  | ✅      |
| 4  | **Test de conexión**     | Script `test_connection.py` operativo | ✅      |
| 5  | **Contenedores activos** | Verificados mediante `docker ps`      | ✅      |
| 6  | **README documentado**   | Incluye arquitectura y guía técnica   | ✅      |
| 7  | **Evidencia visual**     | Captura o video del entorno corriendo | ✅      |

---

## 🧰 Tecnologías Utilizadas

* **Python 3.11**
* **Flask**
* **PostgreSQL 15**
* **Redis 7**
* **Docker & Docker Compose**

---

## 👩‍💻 Autora del Proyecto

**Tracy Moriano**
Ingeniera de Software con Inteligencia Artificial
📍 Lima, Perú — 2025
📧 [tracynicolehmorianotuanama@gmail.com](mailto:tracynicolehmorianotuanama@gmail.com) 

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**, lo que permite su uso, modificación y distribución con los debidos créditos al autor.
