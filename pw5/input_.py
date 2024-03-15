import math
import global_var
from domains.course import Course
from domains.student import Student
from domains.marks import Marks

def input_student_info():
    print("\n*************************")
    print("2. Input student information")
    while True:
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

def input_course_info():
    print("\n*************************")
    print("4. Input course information")
    while True:
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