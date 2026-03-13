def add_student(students, name, grades):
    """
    :param students: dictionary with student name and grades
    :param name: student name
    :param grades: student grade
    :return: if student already in list return None, else updated dict
    """
    if name in students:
        print("Student is already in list")
        return None

    students[name] = grades
    return students

def calculate_average(grades):
    """
    :param grades: list[int] grades
    :return: float, average of grades
    """
    return sum(grades) / len(grades)

def get_grade_letter(average):
    """
    :param average: takes average grade int|float
    :return: returns letter relevant to avg grade "str"
    """
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average <= 89:
        return 'B'
    elif 70 <= average <= 79:
        return 'C'
    elif 60 <= average <= 69:
        return 'D'
    elif 0 <= average <= 59:
        return 'F'

    return "Invalid grade"

def find_top_student(students):
    """
    :param students: dict of students, [str (names) : list[int]]
    :return: fstring top student name and avg
    """
    top_name = None
    max_avg = -1
    for name, grades in students.items():
        avg = calculate_average(grades)
        if avg > max_avg:
            top_name = name
            max_avg = avg
    return f"{top_name} -> {max_avg}"

def get_students_by_grade(students, letter: str):
    """
    :param students: dict of students names and grades
    :param letter: relevant letter to avg, "str"
    :return: dict of students which matches given letter
    """
    students_by_grade = {}
    for name, grades in students.items():
        avg = calculate_average(grades)
        if letter.upper() == get_grade_letter(avg):
            students_by_grade[name] = letter.upper()
    return students_by_grade

if __name__ == "__main__":
    print(calculate_average([50,70,90]))