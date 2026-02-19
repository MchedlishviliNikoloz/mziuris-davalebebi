math_students = {"გიორგი", "ნინო", "დავით", "ანა", "ლევან",
                 "მარიამ", "ნიკა", "თამარ", "გიგა", "სალომე",
                 "ირაკლი", "ნათია", "ლუკა", "ელენე", "გურამ"}
physics_students = {"დავით", "ანა", "ლევან", "ირაკლი", "ნათია", "ლუკა",
                    "ზურა", "კეთი", "ბექა", "მაკა", "ლაშა", "სოფო"}
chemistry_students = {"ლევან", "მარიამ", "ნიკა", "ლუკა", "ელენე", "გურამ",
                      "მაკა", "ლაშა", "სოფო", "ვანო", "ნანა", "თორნიკე", "დარეჯან"}
only_math = math_students.difference(physics_students.union(chemistry_students))
print(only_math)

math_x_physics = math_students.intersection(physics_students)
math_x_chemistry = math_students.intersection(chemistry_students)
physics_x_chemistry = physics_students.intersection(chemistry_students)

min_2_subj = math_x_physics.union(math_x_chemistry).union(physics_x_chemistry)
print(min_2_subj)

subjects = {
    "math": len(math_students),
    "physics": len(physics_students),
    "chemistry": len(chemistry_students)
}
popular = max(subjects, key=subjects.get)
print(popular)