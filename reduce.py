# reduce() = applies a function to an iterable and reduce it to a single cumulative value.
           # Performs a function on first 2 elements and repeats process until 1 value remains

# Purpose: Used to apply a given function to the elements of an iterable in a cumulative way, reducing the iterable to a single value.
# Syntax: reduce(function, iterable, initializer=None)
# Returns: A single value that is the result of applying the function cumulatively to the elements.
# Note: The reduce() function is not a built-in function starting from Python 3.0, and it needs to be imported from the functools module.

import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y, letters)
print(word)

ip = [5,4,3,2,1]
fact = functools.reduce(lambda a,b:a*b, ip)
print(fact)