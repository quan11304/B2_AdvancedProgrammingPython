import numpy as np
import global_var
from domains.course import Course
from domains.student import Student
from domains.marks import Marks


def display_courses():
    print("\n*************************")
    print("6. Display all courses")
    for c in global_var.courses:
        print(c.__str__())


def display_students():
    print("\n*************************")
    print("7. Display all students")
    for s in global_var.students:
        print(s.__str__())


def display_marks():
    print("\n*************************")
    print("8. Display marks of chosen student")

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

    found = []
    for mark in global_var.marks:
        if mark.get_student() == student:
            print(mark.__str__())
            found.append(mark.get_mark())
    print(np.average(np.array(found)))


def sort_gpa():
    list = []
    for student in global_var.students:
        gpa = count = 0
        for mark in global_var.marks:
            if mark.get_student() == student.get_id():
                gpa += mark.get_mark()
                count += 1
        gpa /= count
        list.append((student.get_id(), student.get_name(), gpa))
    array = np.array(list,
                     dtype=[('ID', 'U15'), ('name', 'U30'), ('gpa', 'd')])
    sort_by = np.argsort(array['gpa'])
    print(np.take_along_axis(array, sort_by, 0))

