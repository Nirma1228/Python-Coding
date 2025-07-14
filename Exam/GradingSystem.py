def get_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 45:
        return "C"
    elif avg >= 30:
        return "D"
    else:
        return "F"

students = []

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    marks = []
    for j in range(3):
        mark = int(input(f"Enter mark {j+1} for {name}: "))
        marks.append(mark)
    avg = sum(marks) / len(marks)
    grade = get_grade(avg)
    students.append({"name": name, "marks": marks, "avg": avg, "grade": grade})

print("\nReport:")
for s in students:
    print(f"{s['name']} - Marks: {s['marks']} - Avg: {s['avg']} - Grade: {s['grade']}")

