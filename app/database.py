import sqlite3
from contextlib import contextmanager

sqlite_file_name = 'school.db'

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            country TEXT NOT NULL,
            email TEXT NOT NULL
        )''')
        
        connection.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone INTEGER NOT NULL,
            subject TEXT NOT NULL
        )''')
        
        connection.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_code TEXT NOT NULL,
            credits INTEGER NOT NULL,
            course_teacher TEXT NOT NULL
        )''')


#STUDENT
def add_student(name, age, country, email):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students(name, age, country, email) VALUES (?, ?, ?, ?)',
            (name, age, country, email),
        )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()


#TEACHER 
def add_teacher(name, email, phone, subject):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers(name, email, phone, subject) VALUES (?, ?, ?, ?)',
            (name, email, phone, subject),
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()


#COURSE
def add_course(course_name, course_code, credits, course_teacher):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses(course_name, course_code, credits, course_teacher) VALUES (?, ?, ?, ?)',
            (course_name, course_code, credits, course_teacher),
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()
