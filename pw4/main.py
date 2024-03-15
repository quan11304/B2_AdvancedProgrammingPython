import domains
import input_
import output

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
            input_.input_no_students()
        case "2":
            input_.input_student_info()
        case "3":
            input_.input_no_courses()
        case "4":
            input_.input_course_info()
        case "5":
            input_.input_marks()
        case "6":
            output.display_courses()
        case "7":
            output.display_students()
        case "8":
            output.display_marks()
        case "9":
            output.sort_gpa()
        case "0":
            break
        case _:
            print("Invalid")
