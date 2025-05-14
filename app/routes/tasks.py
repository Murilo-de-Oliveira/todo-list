from fastapi import APIRouter
from app.schemas.task import Task, CreateTask

router = APIRouter()

# Lista em memória com objetos do tipo Task
tasks = [
    Task(id=1, title="Tarefa 1", description="Realizar a tarefa 1", done=False),
    Task(id=2, title="Tarefa 2", description="Realizar a tarefa 2", done=True),
]

@router.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks

@router.post("/tasks", response_model=Task)
def add_task(task_data: CreateTask):
    new_task = Task(id=len(tasks)+1, **task_data.dict())  # Cria Task a partir do CreateTask
    tasks.append(new_task)
    return new_task
