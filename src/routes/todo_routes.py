from fastapi import APIRouter, status
from controllers.todo_controller import get_todos, set_todos
from schema.todos_schema import TodoCreate

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/")
def get_todos_route():
    return get_todos()

@router.post('/', status_code = status.HTTP_201_CREATED)
def set_todos_route(todo: TodoCreate):
    return set_todos(todo)

