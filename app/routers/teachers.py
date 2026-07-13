from fastapi import APIRouter
from services import teachers
from schemas.teachers import Teacher

router = APIRouter(prefix = "/teachers", tags = ["teachers"])

@router.get("/teachers")
def api_list_teachers():
    return teachers.list_teachers()

@router.post("/teachers")
def api_register_teacher(teacher:Teacher):
    return teachers.register_teacher(teacher)

@router.put("/teachers/{teacher_id}")
def api_update_teacher(teacher_id: int, teacher: teachers.Teacher):
    return teachers.update_teacher(teacher_id, teacher)

@router.delete("/teachers/{teacher_id}")
def api_delete_teacher(teacher_id: int):
    return teachers.delete_teacher(teacher_id)
