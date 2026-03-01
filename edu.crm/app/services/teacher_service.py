class TeacherService:
    def __init__(self, data):
        self.data = data

    def list_teachers(self):
        return self.data.teachers

    def get_teacher(self, teacher_id):
        for teacher in self.data.teachers:
            if teacher['id'] == teacher_id:
                return teacher
        return None

    def add_teacher(self, name, email, speciality):
        new_teacher = {
            "id": self.data.next_teacher_id,
            "name": name,
            "email": email,
            "speciality": speciality
        }
        self.data.teachers.append(new_teacher)
        self.data.next_teacher_id += 1
        return new_teacher

    def update_teacher(self, teacher_id, name=None, email=None, speciality=None):
        teacher = self.get_teacher(teacher_id)
        if teacher is None:
            return False
        if name:
            teacher['name'] = name
        if email:
            teacher['email'] = email
        if speciality:
            teacher['speciality'] = speciality
        return True

    def delete_teacher(self, teacher_id):
        for teacher in self.data.teachers:
            if teacher['id'] == teacher_id:
                self.data.teachers.remove(teacher)
                return True
        return False