# [cite_start]API de Gestión de Tareas (To-Do List) [cite: 1]

[cite_start]Este proyecto es una API REST desarrollada con **FastAPI** para gestionar una lista de tareas almacenadas en un archivo JSON local[cite: 7, 8].

## [cite_start]Funcionalidades [cite: 16]
* [cite_start]Crear tareas (`POST /tasks`) [cite: 19]
* [cite_start]Listar todas las tareas (`GET /tasks`) [cite: 21]
* [cite_start]Obtener tarea por ID (`GET /tasks/{id}`) [cite: 23]
* [cite_start]Actualizar estado (`PUT /tasks/{id}`) [cite: 25]
* [cite_start]Eliminar tareas (`DELETE /tasks/{id}`) [cite: 26]

## [cite_start]Requisitos e Instalación [cite: 48]
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno: `.\venv\Scripts\activate` (Windows).
4. Instalar dependencias: `pip install fastapi uvicorn`.

## [cite_start]Cómo ejecutar [cite: 49]
Ejecutar el servidor con:
[cite_start]`uvicorn main:app --reload` [cite: 33]

## [cite_start]Pruebas [cite: 50]
Puedes probar los endpoints en la documentación automática de Swagger en:
[cite_start]`http://localhost:8000/docs` [cite: 29]