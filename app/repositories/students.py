from database import get_connection

def add_student(name, age, country, email):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students(name, age, country, email) VALUES (?, ?, ?, ?)',
            (name, age, country, email),
        )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()
    
    