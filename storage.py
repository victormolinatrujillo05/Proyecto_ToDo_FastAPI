import json
import os

# Nombre del archivo donde se guardan las tareas 
FILE_PATH = "tasks.json"

def load_tasks():
    # Si el archivo no existe, devolvemos una lista vacía
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    # Guarda la lista de tareas en el archivo JSON
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)