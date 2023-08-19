# filter() function is a built-in function that is used to filter elements from an iterable (e.g., a list, tuple, or set) based on a given function (predicate). It returns an iterator (or filter object) containing the elements that satisfy the condition specified by the function.

#filter(function, iterable)


students = [("Dinesh", "A", 24),
            ("Harish", "B", 22),
            ("Sponge", "C", 19),
            ("Kathy", "D", 26),
            ("John", "E", 18),
            ("Ross", "F", 15)]

age = lambda data:data[2] >= 20
can_drink = list(filter(age,students))
for i in can_drink:
    print(i)
print("\n")

non_drink_age = lambda data:data[2] < 20
non_drink_list = list(filter(non_drink_age,students))
for i in non_drink_list:
    print(i)

###############################################################

def is_even(x):
    return x % 2 == 0
numbers = [1,2,3,4,5,6,7,8,9]

even_nums = filter(is_even,numbers)
even_list = list(even_nums)

for i in even_list:
    print(i)
