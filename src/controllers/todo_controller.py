from schema.todos_schema import TodoCreate
from services.todo_service import get_all_todos, set_new_todo

def get_todos():
  return get_all_todos()

def set_todos(todo: TodoCreate):
  return set_new_todo(todo)
