class StudentError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f' Name:{self.first_name}\n Surname:{self.last_name}\n Age:{self.age}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}\n Book:{self.record_book}'

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 26, 'Lia', 'Tayor', 'AN45')
# print(st1)
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
try:
    gr.add_student(st3)
except StudentError as e:
    print(e)
print(gr)
assert gr.find_student('Jobs') == st1
print('Ok')
