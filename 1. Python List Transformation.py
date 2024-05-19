#Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#Task 2: Calculate the average grade and display it.
grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

#Task 3: Replace any grade below 80 with the value Failed.
grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
grades = ["Failed" if grade < 80 else grade for grade in grades]
print(grades)