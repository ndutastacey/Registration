from . import students, teachers, course

def create_tables():
    students.create_table()
    teachers.create_table()
    course.create_table()