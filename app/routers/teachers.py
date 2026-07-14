from fastapi import APIRouter
from schemas.teachers import Teacher
from repositories.teachers import add_teacher, get_teachers

router = APIRouter(prefix = "/teachers", tags = ["teachers"])

@router.get("/")
def api_list_teachers():
    return get_teachers()

@router.post("/")
def api_register_teacher(teacher:Teacher):
    add_teacher(
        teacher.name,
        teacher.email,
        teacher.phone,
        teacher.subject
    )
    return {"message": "Teacher registered", "teacher": teacher}