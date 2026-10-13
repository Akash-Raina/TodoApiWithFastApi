from fastapi import FastAPI
from routes.todo_routes import router as todo_router

app = FastAPI()

app.include_router(todo_router)

@app.get('/')
def root():
  return {"message": "Your Todo app is running"}
