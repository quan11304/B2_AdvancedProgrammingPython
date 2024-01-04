no_courses = 0
no_students = 0
courses = {}  # Key is ID, value is name
students = {}  # Key is ID, value is list of name and DoB
marks = {}  # Key is list of course and student, value is mark.


def input_no_students():
    print("*************************")
    print("1. Input number of students")

def input_student_info():
    print("*************************")
    print("2. Input student information")

def input_no_courses():
    print("*************************")
    print("3. Input number of courses")


def input_course_info():
    print("*************************")
    print("4. Input course information")


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