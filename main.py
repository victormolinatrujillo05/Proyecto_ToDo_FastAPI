from fastapi import FastAPI, HTTPException
from models import Task
from storage import load_tasks, save_tasks

# Configuración principal de la API
app = FastAPI(
    title="Panel de Control de Tareas",
    description="API profesional para gestionar tareas diarias con persistencia en JSON.",
    version="1.0.0"
)

# Etiqueta común para agrupar los endpoints
TAG_NAME = "Gestión de Tareas"

# --- ENDPOINTS ---

@app.get("/tasks", tags=[TAG_NAME])
def get_tasks():
    """Obtiene la lista completa de tareas guardadas."""
    return load_tasks()

@app.post("/tasks", tags=[TAG_NAME])
def create_task(task: Task):
    """Crea una nueva tarea y le asigna un ID automáticamente."""
    tasks = load_tasks()
    
    # Generar un ID automático
    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    
    # Preparamos los datos de la tarea
    task_dict = task.dict()
    task_dict["id"] = new_id
    
    tasks.append(task_dict)
    save_tasks(tasks)
    
    return {"message": "¡Tarea creada con éxito!", "task": task_dict}

@app.get("/tasks/{task_id}", tags=[TAG_NAME])
def get_task(task_id: int):
    """Busca una tarea específica por su número de ID."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tasks/{task_id}", tags=[TAG_NAME])
def update_task(task_id: int, updated_task: Task):
    """Actualiza los datos de una tarea existente manteniendo su ID."""
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            task_dict = updated_task.dict()
            task_dict["id"] = task_id
            tasks[i] = task_dict
            save_tasks(tasks)
            return {"message": "Tarea actualizada correctamente", "task": task_dict}
    raise HTTPException(status_code=404, detail="No se pudo actualizar: ID inexistente")

@app.delete("/tasks/{task_id}", tags=[TAG_NAME])
def delete_task(task_id: int):
    """Elimina una tarea permanentemente de la lista."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="No se encontró la tarea para borrar")
    
    save_tasks(new_tasks)
    return {"message": f"Tarea {task_id} eliminada correctamente"}