class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        marks = [0,1,2,3,4,5,6,7,8,9,10]
        if isinstance(lecturer, Mentor) and grade in marks:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[]
class Lecturer(Mentor):
    def __init__(self, name, surname, grades):
        super().__init__(name, surname)
        self.grades ={}
    def av_gr(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)
            average_grade = round(sum_gr / len_gr)
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_gr()}"
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
cool_lecturer = Lecturer('Some', 'Buddy', grades=10)
cool_lecturer.courses_attached += ['Python']

lecturer1 = Lecturer ('Some', 'Buddy')
student1.rate_lec(lecturer1, 'Sql', 9)
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', grades=())

print(some_reviewer)
print(some_lecturer)