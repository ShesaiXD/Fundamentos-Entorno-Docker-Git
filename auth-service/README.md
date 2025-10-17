# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

## Servicios base
- PostgreSQL (5432)
- Redis (6379)

## Checklist Día 1
- [x] Estructura base creada
- [x] Git inicializado y subido a GitHub
- [x] Docker Compose funcional con PostgreSQL y Redis
- [x] Archivo .env.example configurado
- [x] Test de conexión ejecutado con éxito
