import math
import global_var
from domains.course import Course
from domains.student import Student
from domains.marks import Marks


def input_no_students():
    print("\n*************************")
    print("1. Input number of students")
    while True:
        print("There are currently " + str(global_var.no_students) + " registered "
                                                          "students.")
        global_var.no_students = int(input("Enter the number of students: "))
        if global_var.no_students < len(global_var.students):
            print("Invalid. This value must be equal or greater than the "
                  "number of registered students.")
        else:
            break


def input_student_info():
    print("\n*************************")
    print("2. Input student information")
    while True:
        if len(global_var.students) >= global_var.no_students:
            print("Max number of students reached. Exiting...")
            break

        id_ = input("Enter Student ID: ")
        # Check for duplicates
        br = 0
        for s in global_var.students:
            if id_ == s.get_id():
                br = 1
                print("ID already exists. Please try again.")
                break
        if br == 1:
            continue

        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        s = Student(id_, name, dob)
        global_var.students.add(s)
        print("Student added to record successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 (or any other number) to continue, 0 to quit
            break


def input_no_courses():
    print("\n*************************")
    print("3. Input number of courses")
    while True:
        print("There are currently " + str(global_var.no_courses) + " courses available.")
        global_var.no_courses = int(input("Enter the number of courses: "))
        if global_var.no_courses < len(global_var.courses):
            print("Invalid. This value must be equal or greater than the "
                  "number of existing courses.")
        else:
            break


def input_course_info():
    print("\n*************************")
    print("4. Input course information")
    while True:
        if len(global_var.courses) >= global_var.no_courses:
            print("Max number of courses reached. Exiting...")
            break

        id_ = input("Enter Course ID: ")
        # Check for duplicates
        br = 0
        for c in global_var.courses:
            if id_ == c.get_id():
                br = 1
                print("ID already exists. Please try again.")
                break
        if br == 1:
            continue

        name = input("Enter Course Name: ")
        global_var.courses.add(Course(id_, name))
        print("Course created successfully!")
        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 (or any other number) to continue, 0 to quit
            break


def input_marks():
    print("\n*************************")
    print("5. Input student marks")

    while True:
        br = 0
        while True:
            course = input("Enter Course ID: ")
            for c in global_var.courses:
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
            for s in global_var.students:
                if s.get_id() == student:
                    br = 1
                    break
            if br == 0:
                print("Student not found. Please try again.")
            else:
                break

        mark = math.floor(float(input("Enter Mark: ")) * 10) / 10
        global_var.marks.add(Marks(course, student, mark))

        # if (course, student) in marks.keys():
        #     print("Mark updated successfully")
        # else:
        #     print("Mark registered successfully")

        if not (int(input("Do you want to continue? (1/0): "))):
            # 1 (or any other number) to continue, 0 to quit
            break