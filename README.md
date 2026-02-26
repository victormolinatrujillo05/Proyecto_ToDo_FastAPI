#  Gestión de Tareas - Proyecto FastAPI

¡Hola! Este es mi proyecto para la práctica de desarrollo de APIs. He construido una herramienta para gestionar tareas diarias (To-Do List) donde los datos se guardan de forma local en un archivo JSON.

##  Funcionalidades
He implementado los siguientes endpoints para manejar las tareas:
- **POST /tasks**: Para crear tareas con ID automático.
- **GET /tasks**: Para ver el listado completo.
- **GET /tasks/{id}**: Para buscar una tarea específica.
- **PUT /tasks/{id}**: Para actualizar el estado (marcar como completada).
- **DELETE /tasks/{id}**: Para borrar tareas.

##  Instalación y Uso
Si quieres probarlo, sigue estos pasos:

1. **Entorno virtual**: Crea uno con `python -m venv venv`.
2. **Actívalo**: En Windows usa `.\venv\Scripts\activate`.
3. **Librerías**: Instala todo con `pip install fastapi uvicorn`.
4. **Ejecución**: Lanza el servidor con `uvicorn main:app --reload`.

##  Cómo probar la API (Swagger)
Para interactuar con la API de forma visual, abre tu navegador en: `http://localhost:8000/docs`. Verás un panel con botones de colores; aquí te explico cómo usar cada uno:

### 1. Crear una nueva tarea (POST)
Es el botón verde. Sirve para añadir tareas a tu lista.
* Haz clic en **POST /tasks** y luego en **"Try it out"**.
* En el cuadro de texto (`Request body`), verás un ejemplo en formato JSON. Cambia el "title" y la "description" por lo que quieras.
* Pulsa **"Execute"**. Si todo va bien, verás un código 200 y la tarea se guardará en el archivo `tasks.json` con un ID generado automáticamente.

### 2. Ver todas las tareas (GET)
Es el botón azul superior. Sirve para consultar tu lista completa.
* Haz clic en **GET /tasks** -> **"Try it out"** -> **"Execute"**.
* La API te devolverá un listado de todas las tareas que has creado hasta el momento.

### 3. Buscar una tarea específica (GET por ID)
Sirve para ver los detalles de una sola tarea usando su número identificador.
* Haz clic en **GET /tasks/{task_id}** -> **"Try it out"**.
* Escribe el número del ID (por ejemplo: 1) en el campo correspondiente.
* Pulsa **"Execute"**. Si el ID existe, verás la tarea; si no, la API te avisará de que no se encuentra.

### 4. Actualizar una tarea / Marcar como completada (PUT)
Es el botón naranja. Úsalo para cambiar el título, la descripción o el estado de la tarea.
* Haz clic en **PUT /tasks/{task_id}** -> **"Try it out"**.
* Introduce el ID de la tarea que quieres modificar.
* En el cuadro de texto, cambia "completed": false por "completed": true para marcarla como hecha.
* Pulsa **"Execute"** para guardar los cambios.

### 5. Eliminar una tarea (DELETE)
Es el botón rojo. Úsalo para borrar permanentemente una tarea.
* Haz clic en **DELETE /tasks/{task_id}** -> **"Try it out"**.
* Introduce el ID de la tarea que deseas borrar.
* Pulsa **"Execute"**. Verás un mensaje confirmando que la tarea ha sido eliminada del archivo JSON.

##  Extras añadidos
Para que el proyecto sea más profesional, he incluido:
- **Validación con Pydantic**: Para asegurar que los datos son correctos.
- **Estructura modular**: Código organizado en diferentes archivos.
- **Dockerfile**: Listo para ejecutar la aplicación en un contenedor.

