from fastapi import FastAPI
from models import Task
from storage import load_tasks, save_tasks

app = FastAPI(title="Mi API de Tareas")

# Endpoint para obtener todas las tareas [cite: 21]
@app.get("/tasks")
def get_tasks():
    return load_tasks()

# Endpoint para crear una nueva tarea [cite: 19]
@app.post("/tasks")
def create_task(task: Task):
    tasks = load_tasks()
    
    # Generar un ID automático [cite: 12]
    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    
    # Preparamos los datos de la tarea [cite: 10]
    task_dict = task.dict()
    task_dict["id"] = new_id
    
    tasks.append(task_dict)
    save_tasks(tasks)
    
    return {"message": "Tarea creada!", "task": task_dict}
from fastapi import HTTPException # Añade esto arriba, junto a los otros imports

# 1. Obtener una tarea por su ID [cite: 22]
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# 2. Actualizar una tarea (marcar como completada) [cite: 24]
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            # Mantener el ID original pero actualizar el resto [cite: 25]
            task_dict = updated_task.dict()
            task_dict["id"] = task_id
            tasks[i] = task_dict
            save_tasks(tasks)
            return {"message": "Tarea actualizada", "task": task_dict}
    raise HTTPException(status_code=404, detail="No se pudo actualizar")

# 3. Eliminar una tarea 
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="No se encontró la tarea para borrar")
    
    save_tasks(new_tasks)
    return {"message": f"Tarea {task_id} eliminada correctamente"}