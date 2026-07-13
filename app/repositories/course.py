from database import get_connection

def add_course(course_name, course_code, credits, course_teacher):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses(course_name, course_code, credits, course_teacher) VALUES (?, ?, ?, ?)',
            (course_name, course_code, credits, course_teacher),
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()
    