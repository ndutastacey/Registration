from fastapi import FastAPI
from models import create_tables
from routers import teachers, course, students 

app = FastAPI()

create_tables()

app.include_router(teachers.router)
app.include_router(course.router)
app.include_router(students.router)
