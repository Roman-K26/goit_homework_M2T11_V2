from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Todo
from src.schemas.todo import  TodoSchema, TodoResponse, TodoUpdateSchema

# робота з базою даних
async def get_todos(limit: int, offset: int, db: AsyncSession):
    stmt = select(Todo).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_todo(todo_id: int, db: AsyncSession):
    stmt = select(Todo).filter_by(id=todo_id)
    todo = await db.execute(stmt)
    return todo.scalar_one_or_none()


async def create_todo(body: TodoSchema, db: AsyncSession):
    todo = Todo(**body.model_dump(exclude_unset=True))
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo




async def update_todo():
    pass


async def delete_todo():
    pass