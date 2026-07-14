from fastapi import APIRouter
from schemas.students import Student
from repositories.students import add_student, get_students

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/")
def api_list_students():
    return get_students()

@router.post("/")
def api_register_student(student: Student):
    add_student(
        student.name,
        student.age,
        student.country,
        student.email
    )
    return {"message": "Student registered", "student": student}
