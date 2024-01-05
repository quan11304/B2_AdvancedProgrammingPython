no_courses = 0
no_students = 0
courses = {}  # Key is ID, value is name
students = {}  # Key is ID, value is list of name and DoB
marks = {}  # Key is list of course and student, value is mark.


def input_no_students():
    global no_students, students
    print("*************************")
    print("1. Input number of students")
    while True:
        no_students = int(input("Enter the number of students: "))
        if no_students < len(students):
            print("Invalid. This value must be equal or greater than the "
                  "number of registered students.")
        else:
            break


def input_student_info():
    global no_students, students
    print("*************************")
    print("2. Input student information")
    while True:
        ID = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth: ")
        students[ID] = (name, dob)
        print("Student added to record successfully!")
        if len(students) < no_students:
            print("Max number of students reached. Exiting...")
            break
        elif not (bool(input("Do you want to continue? (1/0)"))):
            break


def input_no_courses():
    global no_courses, courses
    print("*************************")
    print("3. Input number of courses")
    while True:
        print("There are currently " + no_courses + " courses available.")
        no_courses = int(input("Enter the number of courses: "))
        if no_courses < len(courses):
            print("Invalid. This value must be equal or greater than the "
                  "number of existing courses.")
        else:
            break


def input_course_info():
    global no_courses, courses
    print("*************************")
    print("4. Input course information")
    while True:
        ID = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        courses[ID] = name
        print("Course created successfully!")
        if len(courses) < no_courses:
            print("Max number of courses reached. Exiting...")
            break
        elif not (bool(input("Do you want to continue? (1/0)"))):
            break


def input_marks():
    print("*************************")
    print("5. Input student marks")


def display_courses():
    print("*************************")
    print("6. Display all courses")


def display_students():
    print("*************************")
    print("7. Display all students")


def display_marks():
    print("*************************")
    print("8. Display marks of chosen student")


while (True):
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
    *************************
    """)

    choice = input("Choose the next action by entering the respective "
                   "number: ")

    match choice:
        case 1:
            continue
        case 2:
            continue
        case 3:
            continue
        case 4:
            continue
        case 5:
            continue
        case 6:
            continue
        case 7:
            continue
        case 8:
            continue
        case 0:
            break
        case _:
            print("Invalid")