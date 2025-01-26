student_count = int(input())
students_info = {}

for _ in range(student_count):
    name, grade = input().split()

    if name not in students_info:
        students_info[name] = []
    students_info[name].append(float(grade))

for name, grades in students_info.items():
    formatted_grades = [str(f'{grade:.2f}') for grade in grades]
    average_grades = sum(grades) / len(grades)
    print(f'{name} -> {" ".join(formatted_grades)} (avg: {average_grades:.2f})')
