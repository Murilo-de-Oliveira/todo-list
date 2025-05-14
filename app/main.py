from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(title="ToDo List API")

app.include_router(tasks.router, prefix="/tasks", tags=["Tarefas"])

@app.get("/")
def read_root():
    return {"mensagem": "API de ToDo está rodando!"}