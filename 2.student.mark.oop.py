no_courses = 0
no_students = 0
courses = set()
students = set()
marks = set()


class Course:
    def __init__(self, id_, name):
        self.__id = id_
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__id} - {self.__name}'


class Student:
    def __init__(self, id_, name, dob):
        self.__id = id_
        self.__name = name
        self.__dob = dob

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    def __str__(self):
        return f'{self.__id} - {self.__name} - {self.__dob}'


class Marks:
    def __init__(self, course, student, mark):
        self.__course = course
        self.__student = student
        self.__mark = mark

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        self.__course = course

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        self.__student = student

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    def __str__(self):
        return f'{self.__course} - {self.__student} - {self.__mark}\n'


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
        ID = input("Enter Student ID: ")
        if ID in students.keys():
            print("ID already exists. Please try again.")
            continue
        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        students[ID] = (name, dob)
        print("Student added to record successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 to continue, 0 to quit
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
        ID = input("Enter Course ID: ")
        if ID in courses.keys():
            print("ID already exists. Please try again")
            continue
        name = input("Enter Course Name: ")
        courses[ID] = name
        print("Course created successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            break


def input_marks():
    print("\n*************************")
    print("5. Input student marks")
    while True:
        course = input("Enter Course ID: ")
        if course not in courses.keys():
            print("Course not found. Please try again.")
        else:
            break
    while True:
        student = input("Enter Student ID: ")
        if student not in students.keys():
            print("Student not found. Please try again.")
        else:
            break
    mark = int(input("Enter Mark: "))
    marks[(course, student)] = mark
    if (course, student) in marks.keys():
        print("Mark updated successfully")
    else:
        print("Mark registered successfully")


def display_courses():
    print("\n*************************")
    print("6. Display all courses")
    for c in courses:
        c.__str__()


def display_students():
    print("\n*************************")
    print("7. Display all students")
    for s in students:
        s.__str__()


def display_marks():
    print("\n*************************")
    print("8. Display marks of chosen student")
    while True:
        s = input("Enter Student ID: ")
        if s not in students:
            print("Student not found. Please try again.")
        else:
            break
    for mark in marks:
        if mark[1] == s:
            mark.__str__()


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
        case "0":
            break
        case _:
            print("Invalid")
