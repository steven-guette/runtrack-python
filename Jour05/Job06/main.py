from random import randint
import includes.functions as func

minMark = 0
maxMark = 100

students = {
    "cédric" : 0,
    "benoit" : 0,
    "valéria" : 0,
    "Philippe" : 0,
}

for student in students:
    students[student] = randint(minMark, maxMark)

    print(f"{student.capitalize()} => ( {students[student]} | {func.GetStudentMarkRounded(students[student])} )")