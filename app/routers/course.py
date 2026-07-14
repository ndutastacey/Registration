from fastapi import APIRouter
from schemas.course import Course
from repositories.course import add_course, get_courses

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/courses")
def api_list_courses():
    return get_courses()

@router.post("/courses")
def api_register_course(course:Course):
    add_course(
        course.course_name,
        course.course_code,
        course.credits,
        course.course_teacher
    )
    return {"message": "Course registered", "course": course}


