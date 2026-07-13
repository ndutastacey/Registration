from pydantic import BaseModel

class Course(BaseModel):
    course_name: str
    course_code: str
    credits: int
    course_teacher: str