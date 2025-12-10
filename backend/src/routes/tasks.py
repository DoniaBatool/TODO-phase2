"""Task CRUD API endpoints."""

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from src.db import get_session
from src.models import Task
from src.schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(tags=["Tasks"])


@router.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    task_data: TaskCreate,
    session: Session = Depends(get_session)
):
    """
    Create a new task.
    
    Args:
        task_data: Task creation data
        session: Database session
    
    Returns:
        TaskResponse: Created task with generated ID and timestamps
    
    Raises:
        HTTPException: 400 if validation fails, 500 if database error
    """
    try:
        # Create new task from request data
        task = Task(
            user_id=task_data.user_id,
            title=task_data.title,
            description=task_data.description,
        )
        
        # Add to database
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return task
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create task: {str(e)}"
        ) from e


@router.get("/tasks", response_model=List[TaskResponse])
async def list_tasks(
    completed: Optional[bool] = Query(default=None, description="Filter by completion status"),
    session: Session = Depends(get_session)
):
    """
    List all tasks with optional filtering by completion status.
    
    Args:
        completed: Optional filter for task completion status
        session: Database session
    
    Returns:
        List[TaskResponse]: List of tasks matching filter
    """
    try:
        # Build query
        statement = select(Task)
        
        # Apply filter if provided
        if completed is not None:
            statement = statement.where(Task.completed == completed)
        
        # Execute query
        tasks = session.exec(statement).all()
        
        return tasks
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve tasks: {str(e)}"
        ) from e


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Get a specific task by ID.
    
    Args:
        task_id: Task ID to retrieve
        session: Database session
    
    Returns:
        TaskResponse: Task data
    
    Raises:
        HTTPException: 404 if task not found
    """
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    session: Session = Depends(get_session)
):
    """
    Update an existing task.
    
    Args:
        task_id: Task ID to update
        task_data: Updated task data
        session: Database session
    
    Returns:
        TaskResponse: Updated task
    
    Raises:
        HTTPException: 404 if task not found, 400 if validation fails
    """
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    
    try:
        # Update fields if provided
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        
        # Update timestamp
        task.updated_at = datetime.utcnow()
        
        # Save changes
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return task
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to update task: {str(e)}"
        ) from e


@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
async def toggle_task_completion(
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Toggle task completion status.
    
    Args:
        task_id: Task ID to toggle
        session: Database session
    
    Returns:
        TaskResponse: Updated task
    
    Raises:
        HTTPException: 404 if task not found
    """
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    
    try:
        # Toggle completion status
        task.completed = not task.completed
        task.updated_at = datetime.utcnow()
        
        # Save changes
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return task
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to toggle task completion: {str(e)}"
        ) from e


@router.delete("/tasks/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Delete a task.
    
    Args:
        task_id: Task ID to delete
        session: Database session
    
    Raises:
        HTTPException: 404 if task not found
    """
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    
    try:
        session.delete(task)
        session.commit()
        return None  # 204 No Content
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to delete task: {str(e)}"
        ) from e

