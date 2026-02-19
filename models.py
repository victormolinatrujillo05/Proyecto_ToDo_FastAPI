from pydantic import BaseModel
from typing import Optional

# Este es el modelo que usará Pydantic para validar los datos [cite: 39]
class Task(BaseModel):
    id: Optional[int] = None      # Identificador único [cite: 12]
    title: str                    # Título de la tarea [cite: 13]
    description: Optional[str] = None # Descripción opcional [cite: 14]
    completed: bool = False       # Estado: pendiente o completada [cite: 15]