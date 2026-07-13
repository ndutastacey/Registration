from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_code TEXT NOT NULL,
            credits INTEGER NOT NULL,
            course_teacher TEXT NOT NULL
        )''')