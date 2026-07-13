from database import get_connection

def add_teacher(name, email, phone, subject):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers(name, email, phone, subject) VALUES (?, ?, ?, ?)',
            (name, email, phone, subject),
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()
    