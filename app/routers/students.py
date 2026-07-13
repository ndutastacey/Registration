from fastapi import APIRouter

from services import students
from schemas.students import Student

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/")
def home():
    return {"message": "Welcome to my API server"}

@router.get("/students")
def get_students_list():
    return students

@router.post("/students")
def create_student(student: Student):
    student.add_student(student.name, student.age, student.country, student.email)
    students.append(student)
    return {"message": "Student registered", "student": student}

@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if i == student_id:
            students[i] = student
            return {"message": "Student updated", "student": student}
    return {"message": "Student not found"}

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if i == student_id:
            del students[i]
            return {"message": "Student deleted"}
    return {"message": "Student not found"}
