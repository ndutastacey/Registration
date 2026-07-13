from schemas.students import Student

def get_students_list():
    return students

def create_student(student: Student):
    database.add_student(student.name, student.age, student.country, student.email)
    students.append(student)
    return {"message": "Student registered", "student": student}

def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if i == student_id:
            students[i] = student
            return {"message": "Student updated", "student": student}
    return {"message": "Student not found"}

def delete_student(student_id: int):
    for i, s in enumerate(students):
        if i == student_id:
            del students[i]
            return {"message": "Student deleted"}
    return {"message": "Student not found"}
