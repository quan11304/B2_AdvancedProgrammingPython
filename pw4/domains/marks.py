class Marks:
    def __init__(self, course, student, mark):
        self.__course = course
        self.__student = student
        self.__mark = mark

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def __str__(self):
        return f'{self.__course} - {self.__student} - {self.__mark}'

