# a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

#general way of writing
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

#list = [expression for item in iterable]
squares = [i * i for i in range(1,11)]
print(squares)

marks = [100,90,70,60,30,20,10,35,0]
failed_students = []
#passed_students = list(filter(lambda x: x<=35, marks))
passed_students = [i if i >= 35 else failed_students.append(i) for i in marks]
print(passed_students)
print(failed_students)