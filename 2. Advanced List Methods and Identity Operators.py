#Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = set(submitted) & set(attended)
print("Students who both submitted assignments and attended the class:", both)

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted.sort()
attended.sort()

if submitted == attended:
    print("The lists are identical in terms of their content.")
else:
    print("The lists are not identical in terms of their content.")

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended = [student for student in attended if student in submitted]
print("Attended list after removing students who did not submit their assignment:", attended)