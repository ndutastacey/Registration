from fastapi import FastAPI
from pydantic import BaseModel
import database
import teachers 
import course    

app = FastAPI()

database.create_table()

class Student(BaseModel):
    name: str
    age: int
    country: str
    email: str

students = []

@app.get("/")
def home():
    return {"message": "Welcome to my API server"}

@app.get("/students")
def get_students_list():
    return students

@app.post("/students")
def create_student(student: Student):
    database.add_student(student.name, student.age, student.country, student.email)
    students.append(student)
    return {"message": "Student registered", "student": student}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if i == student_id:
            students[i] = student
            return {"message": "Student updated", "student": student}
    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if i == student_id:
            del students[i]
            return {"message": "Student deleted"}
    return {"message": "Student not found"}

#############################################################################################################

@app.get("/teachers")
def api_list_teachers():
    return teachers.list_teachers()

@app.post("/teachers")
def api_register_teacher(teacher: teachers.Teacher):
    return teachers.register_teacher(teacher)

@app.put("/teachers/{teacher_id}")
def api_update_teacher(teacher_id: int, teacher: teachers.Teacher):
    return teachers.update_teacher(teacher_id, teacher)

@app.delete("/teachers/{teacher_id}")
def api_delete_teacher(teacher_id: int):
    return teachers.delete_teacher(teacher_id)

#############################################################################################################

@app.get("/courses")
def api_list_courses():
    return course.list_courses()

@app.post("/courses")
def api_register_course(c: course.Course):
    return course.register_course(c)

@app.put("/courses/{course_id}")
def api_update_course(course_id: int, c: course.Course):
    return course.update_course(course_id, c)

@app.delete("/courses/{course_id}")
def api_delete_course(course_id: int):
    return course.delete_course(course_id)
