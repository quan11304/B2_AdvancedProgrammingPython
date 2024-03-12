import math
import numpy as np

no_courses = 0
no_students = 0
courses = set()
students = set()
marks = set()


class Course:
    def __init__(self, id_, name):
        self.__id = id_
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id_):
        self.__id = id_

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__id} - {self.__name}'


class Student:
    def __init__(self, id_, name, dob):
        self.__id = id_
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def set_id(self, id_):
        self.__id = id_

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def __str__(self):
        return f'{self.__id} - {self.__name} - {self.__dob}'


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


def input_no_students():
    global no_students
    print("\n*************************")
    print("1. Input number of students")
    while True:
        print("There are currently " + str(no_students) + " registered "
                                                          "students.")
        no_students = int(input("Enter the number of students: "))
        if no_students < len(students):
            print("Invalid. This value must be equal or greater than the "
                  "number of registered students.")
        else:
            break


def input_student_info():
    print("\n*************************")
    print("2. Input student information")
    while True:
        if len(students) >= no_students:
            print("Max number of students reached. Exiting...")
            break

        id_ = input("Enter Student ID: ")
        # Check for duplicates
        br = 0
        for s in students:
            if id_ == s.get_id():
                br = 1
                print("ID already exists. Please try again.")
                break
        if br == 1:
            continue

        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        s = Student(id_, name, dob)
        students.add(s)
        print("Student added to record successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 (or any other number) to continue, 0 to quit
            break


def input_no_courses():
    global no_courses
    print("\n*************************")
    print("3. Input number of courses")
    while True:
        print("There are currently " + str(no_courses) + " courses available.")
        no_courses = int(input("Enter the number of courses: "))
        if no_courses < len(courses):
            print("Invalid. This value must be equal or greater than the "
                  "number of existing courses.")
        else:
            break


def input_course_info():
    print("\n*************************")
    print("4. Input course information")
    while True:
        if len(courses) >= no_courses:
            print("Max number of courses reached. Exiting...")
            break

        id_ = input("Enter Course ID: ")
        # Check for duplicates
        br = 0
        for c in courses:
            if id_ == c.get_id():
                br = 1
                print("ID already exists. Please try again.")
                break
        if br == 1:
            continue

        name = input("Enter Course Name: ")
        courses.add(Course(id_, name))
        print("Course created successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 (or any other number) to continue, 0 to quit
            break


def input_marks():
    print("\n*************************")
    print("5. Input student marks")

    br = 0
    while True:
        course = input("Enter Course ID: ")
        for c in courses:
            if c.get_id() == course:
                br = 1
                break
        if br == 0:
            print("Course not found. Please try again.")
        else:
            break

    br = 0
    while True:
        student = input("Enter Student ID: ")
        for s in students:
            if s.get_id() == student:
                br = 1
                break
        if br == 0:
            print("Student not found. Please try again.")
        else:
            break

    mark = math.floor(float(input("Enter Mark: ")) * 10) / 10
    marks.add(Marks(course, student, mark))
    # if (course, student) in marks.keys():
    #     print("Mark updated successfully")
    # else:
    #     print("Mark registered successfully")


def display_courses():
    print("\n*************************")
    print("6. Display all courses")
    for c in courses:
        print(c.__str__())


def display_students():
    print("\n*************************")
    print("7. Display all students")
    for s in students:
        print(s.__str__())


def display_marks():
    print("\n*************************")
    print("8. Display marks of chosen student")

    br = 0
    while True:
        student = input("Enter Student ID: ")
        for s in students:
            if s.get_id() == student:
                br = 1
                break
        if br == 0:
            print("Student not found. Please try again.")
        else:
            break

    found = []
    for mark in marks:
        if mark.get_student() == student:
            print(mark.__str__())
            found.append(mark.get_mark())
    print(np.average(np.array(found)))


def sort_gpa():
    list = []
    for student in students:
        gpa = count = 0
        for mark in marks:
            if mark.get_student() == student.get_id():
                gpa += mark.get_mark()
                count += 1
        gpa /= count
        list.append((student.get_id(), student.get_name, gpa))
    array = np.array(list,dtype=[('ID','U15'),('name','U30'),('gpa','d')])
    


# Main programme
while True:
    print("""
*************************
1. Input number of students
2. Input student information
3. Input number of courses
4. Input course information
5. Input student marks
6. Display all courses
7. Display all students
8. Display marks of chosen student
9. Sort student list by GPA
0. Exit
*************************""")

    choice = input("Choose the next action by entering the respective "
                   "number: ")

    match choice:
        case "1":
            input_no_students()
        case "2":
            input_student_info()
        case "3":
            input_no_courses()
        case "4":
            input_course_info()
        case "5":
            input_marks()
        case "6":
            display_courses()
        case "7":
            display_students()
        case "8":
            display_marks()
        case "9":
            sort_gpa()
        case "0":
            break
        case _:
            print("Invalid")
