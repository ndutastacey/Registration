from pydantic import BaseModel
import database 

class Course(BaseModel):
    course_name: str
    course_code: str
    credits: int
    course_teacher: str

courses = []

def list_courses():
    return courses

def register_course(course: Course):
    database.add_course(course.course_name, course.course_code, course.credits, course.course_teacher)
    courses.append(course)
    return {"message": "Course registered", "course": course}

def update_course(course_id: int, course: Course):
    for i, c in enumerate(courses):
        if i == course_id:
            courses[i] = course
            return {"message": "Course updated", "course": course}
    return {"message": "Course not found"}

def delete_course(course_id: int):
    for i, c in enumerate(courses):
        if i == course_id:
            del courses[i]
            return {"message": "Course deleted"}
    return {"message": "Course not found"}
