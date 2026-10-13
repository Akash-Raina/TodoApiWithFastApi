from pydantic import BaseModel

class TodoCreate(BaseModel):
  title: str
  description: str | None = None
  completed: bool = False
