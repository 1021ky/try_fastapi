from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.api.cruds.tasks as task_crud
from app.api.db import get_db
from app.api.schemas import task as task_schema

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass


@router.post("/tasks")
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())
