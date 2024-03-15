import input_
import output

# Main programme
while True:
    print("""
*************************
1. Input student information
2. Input course information
3. Input student marks
4. Display all courses
5. Display all students
6. Display marks of chosen student
7. Sort student list by GPA
0. Exit
*************************""")

    choice = input("Choose the next action by entering the respective "
                   "number: ")

    match choice:
        case "1":
            input_.input_student_info()
        case "2":
            input_.input_course_info()
        case "3":
            input_.input_marks()
        case "4":
            output.display_courses()
        case "5":
            output.display_students()
        case "6":
            output.display_marks()
        case "7":
            output.sort_gpa()
        case "0":
            break
        case _:
            print("Invalid")
