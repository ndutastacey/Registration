from schemas.teachers import Teacher

teachers = []

def list_teachers():
    return teachers

def register_teacher(teacher: Teacher):
    Teacher.add_teacher(teacher.name, teacher.email, teacher.phone, teacher.subject)
    teachers.append(teacher)
    return {"message": "Teacher registered", "teacher": teacher}

def update_teacher(teacher_id: int, teacher: Teacher):
    for i, t in enumerate(teachers):
        if i == teacher_id:
            teachers[i] = teacher
            return {"message": "Teacher updated", "teacher": teacher}
    return {"message": "Teacher not found"}

def delete_teacher(teacher_id: int):
    for i, t in enumerate(teachers):
        if i == teacher_id:
            del teachers[i]
            return {"message": "Teacher deleted"}
    return {"message": "Teacher not found"}
