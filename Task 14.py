from modules.student_manager import *
students = {
    "Name" : [56, 32, 86],
}

add_student(students,"abc",[81,26,74])
add_student(students,"utoroe",[54,12,76])
print(add_student(students,"top",[97,96,99]))
print(calculate_average([81,26,74]))
print(get_grade_letter(calculate_average([81,26,74])))
print(find_top_student(students))
print(get_students_by_grade(students, "F"))