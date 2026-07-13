from fastapi import APIRouter
from services import course
from schemas.course import Course

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("/courses")
def api_list_courses():
    return course.list_courses()

@router.post("/courses")
def api_register_course(c:Course):
    return course.register_course(c)

@router.put("/courses/{course_id}")
def api_update_course(course_id: int, c: course.Course):
    return course.update_course(course_id, c)

@router.delete("/courses/{course_id}")
def api_delete_course(course_id: int):
    return course.delete_course(course_id)
