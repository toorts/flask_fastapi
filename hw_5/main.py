from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()


# Модель Pydantic для задачи
class Task(BaseModel):
    title: str
    description: str
    status: bool

# Список задач в памяти (вместо базы данных для простоты)
tasks_db = []


# Конечная точка для получения списка всех задач
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db


# Конечная точка для получения задачи по идентификатору
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


# Конечная точка для создания новой задачи
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task


# Конечная точка для обновления задачи по идентификатору
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task


# Конечная точка для удаления задачи по идентификатору
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks_db.pop(task_id)
    return deleted_task


# Запуск сервера с помощью uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
