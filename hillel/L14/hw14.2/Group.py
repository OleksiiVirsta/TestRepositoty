from StudentError import StudentError

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        n = 0
        for st in self.group:
            n += 1
        if n >= 2:
            raise StudentError('Забагато')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is None:
            return 'No student!'
        else:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        n = 0
        for st in self.group:
            all_students += f'\nStudent: {st.first_name} {st.last_name}'
            n += 1
        if n == 0:
            return f'In group {self.number} not have students!'
        elif n == 1:
            return f'Only one student!'
        else:
            return f'In group {self.number} have {n} students:{all_students}'
