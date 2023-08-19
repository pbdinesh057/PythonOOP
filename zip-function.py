# aggregate elements from two or more iterables (list, tuples, sets, etc..)
# creates a zip object with paired elements from each iterable stored in tuples for each element

# Creating zip objects and iterating through paired elements
Usernames = ["Dude", "Bro", "Mister"]
Password = ("P@ssword", "abc123", "Hello")

# Create a zip object that pairs elements from both iterables
users = zip(Usernames, Password)

# Iterating through the zip object to print paired elements
for i in users:
    print(i)
print("\n")

# Creating a dictionary using zip and iterating through the dictionary
users1 = dict(zip(Usernames, Password))

# Printing the type of the created dictionary
print(type(users1))

# Iterating through the dictionary to print keys and values
for key, value in users1.items():
    print(key + ": " + value)


######################################################################################################################

# Aggregating elements from multiple lists using zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
scores = [95, 85, 75]

# Creating a list of tuples by pairing elements from multiple lists
students = list(zip(names, ages, scores))
print(students)

# Unpacking and printing the aggregated elements from the list of tuples
for name, age, score in students:
    print(f"Name: {name}, Age: {age}, Score: {score}")

# Creating a dictionary using zip and unpacking keys and values
student_dict = dict(zip(names, ages))
print(student_dict)

# Aggregating elements from lists of unequal lengths
names = ["Alice", "Bob", "Charlie"]
scores = [95, 85]

# Creating a list of tuples using zip (stops when the shortest list is exhausted)
student_scores = list(zip(names, scores))
print(student_scores)
