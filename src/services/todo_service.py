from schema.todos_schema import TodoCreate

_todos = []
_next_id = 1

def get_all_todos():
  return {"message": "List of all the todos"}

def set_new_todo(todo: TodoCreate):
  global _next_id

  _todos.append(todo)
  _next_id += 1

  return todo
