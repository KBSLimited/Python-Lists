#Task 1: Given the lists:
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_students = [(student, grade, activity) for student, grade, activity in zip(students, grades, activities) if grade >= 80]

for student, grade, activity in filtered_students:
    print(student, grade, activity)

#Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_students = [(student, grade, activity) for student, grade, activity in zip(students, grades, activities) if grade >= 80]

students_approved = [student for student, _, _ in filtered_students]

print("students_approved =", students_approved)

#Task 3: Print the list students_approved
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_students = [(student, grade, activity) for student, grade, activity in zip(students, grades, activities) if grade >= 80]

students_approved = [student for student, _, _ in filtered_students]

print(students_approved)