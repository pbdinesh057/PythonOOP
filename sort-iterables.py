# Sort will only work with Lists

# Sorting a list of strings in reverse alphabetical order
students = ["Dinesh", "Harish", "Prasanna", "Suresh"]
students.sort(reverse=True)  # Sort the list in reverse order
for i in students:
    print(i)
print("\n")

# For Tuples data
students1 = ("Dinesh", "Harish", "Prasanna", "Suresh")
sorted_students = sorted(students1)  # Sort the tuple and return a new sorted list
for i in sorted_students:
    print(i)

# Other data set: list of tuples
students2 = [
    ("Dinesh", "A", 24),
    ("Harish", "B", 22),
    ("Sponge", "C", 19),
    ("Kathy", "D", 26)
]

students2.sort()  # Sort the list of tuples based on the default order (by first element of each tuple)
for i in students2:
    print(i)
print("\n")

# Sorting the list of tuples based on the second element (grade)
grade = lambda grades: grades[1]
students2.sort(key=grade, reverse=True)  # Sort by grade in reverse order
for i in students2:
    print(i)
print("\n")

# Sorting the list of tuples based on the third element (age)
age = lambda ages: ages[2]
students2.sort(key=age)  # Sort by age
for j in students2:
    print(j)
