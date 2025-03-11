from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Course(BaseModel):
    id: int
    name: str
    description: str

courses = [
    Course(id=1, name="Python для новичков", description="Основы Python с практикой."),
    Course(id=2, name="Docker", description="Контейнеризация и работа с Docker."),
    Course(id=3, name="Kubernetes", description="Оркестрация контейнеров в Kubernetes."),
    Course(id=4, name="Git", description="Система контроля версий Git и GitHub."),
]

@app.get("/courses", response_model=List[Course])
def get_courses():
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
