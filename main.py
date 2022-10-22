class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def _average_rate(self):
        sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                counter += 1
        return sum / counter

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student!")
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'''
        Имя:{self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {round(self._average_rate(), 1)}
        Курсы в процессе изучения: {",".join(self.courses_in_progress)}
        Завершенные курсы: {",".join(self.finished_courses)}
        '''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                counter += 1
        return sum / counter

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a lecturer!")
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {round(self._average_rate(), 1)}
        '''
        return res


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
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        '''
        return res


leman_russ = Lecturer('Leman', 'Russ')
leman_russ.courses_attached += ['Python']
leman_russ.courses_attached += ['Technology']

roboute_guilliman = Lecturer('Roboute', 'Guilliman')
roboute_guilliman.courses_attached += ['Chemistry']
roboute_guilliman.courses_attached += ['Magic']
roboute_guilliman.courses_attached += ['Python']

corvus_corax = Student('Corvus', 'Corax', 'm')
corvus_corax.courses_in_progress += ['Python']
corvus_corax.courses_in_progress += ['Technology']
corvus_corax.finished_courses += ['Chemistry']
corvus_corax.finished_courses += ['Magic']

rogal_dorn = Student('Rogal', 'Dorn', 'm')
rogal_dorn.courses_in_progress += ['Chemistry']
rogal_dorn.courses_in_progress += ['Magic']
rogal_dorn.courses_in_progress += ['Python']
rogal_dorn.finished_courses += ['Technology']

horus_lupercal = Reviewer('Horus', 'Lupercal')
horus_lupercal.courses_attached += ['Chemistry']
horus_lupercal.courses_attached += ['Magic']

konrad_curze = Reviewer('Konrad', 'Curze')
konrad_curze.courses_attached += ['Python']
konrad_curze.courses_attached += ['Technology']

lion_eljonson = Mentor("Lion", "El'Jonson")
ferrus_manus = Mentor('Ferrus', 'Manus')

horus_lupercal.rate_hw(rogal_dorn, 'Chemistry', 10)
horus_lupercal.rate_hw(rogal_dorn, 'Magic', 10)
konrad_curze.rate_hw(rogal_dorn, 'Python', 6)
konrad_curze.rate_hw(corvus_corax, 'Python', 9)
konrad_curze.rate_hw(corvus_corax, 'Technology', 10)

corvus_corax.rate_hw(leman_russ, 'Python', 10)
corvus_corax.rate_hw(roboute_guilliman, 'Python', 8)
corvus_corax.rate_hw(leman_russ, 'Technology', 8)
rogal_dorn.rate_hw(roboute_guilliman, 'Chemistry', 9)
rogal_dorn.rate_hw(roboute_guilliman, 'Magic', 10)
rogal_dorn.rate_hw(leman_russ, 'Python', 7)

print(corvus_corax)
print(rogal_dorn)
print(corvus_corax < rogal_dorn)
print(rogal_dorn < corvus_corax)
print(leman_russ)
print(roboute_guilliman)
print(horus_lupercal)
print(konrad_curze)

def av_grade_student(list, course):
    sum = 0
    counter = 0
    for student in list:
        for grade in student.grades[course]:
            sum += grade
            counter += 1
    return round(sum / counter, 1)

def av_grade_lecturer(list, course):
    sum = 0
    counter = 0
    for lecturer in list:
        for grade in lecturer.grades[course]:
            sum += grade
            counter += 1
    return round(sum / counter, 1)

print(f'Средняя оценка за домашние задания в рамках курса: {av_grade_student([corvus_corax, rogal_dorn], "Python")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса: {av_grade_lecturer([leman_russ, roboute_guilliman], "Python")}')