# A function that either
   # a. accepts function as a argument
#            (or)
   # b. returns a function


# Define a function 'loud' that takes a 'text' argument and returns the uppercase version of the text.
def loud(text):
    return text.upper()

# Define a function 'quiet' that takes a 'text' argument and returns the lowercase version of the text.
def quiet(text):
    return text.lower()

# Define a higher-order function 'hello' that takes a 'func' argument, which is expected to be a function.
def hello(func):
    # Call the function 'func' with the argument "Hello" and store the result in the variable 'text'.
    text = func("Hello")
    # Print the value of 'text'.
    print(text)

# Call the 'hello' function with 'quiet' as an argument.
hello(quiet)

# Call the 'hello' function with 'loud' as an argument.
hello(loud)

###############################################################################################################

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate(operation, x, y):
    result = operation(x, y)
    print("Result:", result)

calculate(add, 5, 3)
calculate(subtract, 10, 4)
calculate(multiply, 6, 2)
calculate(divide, 15, 3)

############returns a function

def dr(x):
    def nr(y):
        return y/x
    return nr
z = dr(2)

print(z(10))


###################

def power_of(base):
    def exponent(exp):
        return base ** exp
    return exponent

# Create functions for specific bases
square = power_of(2)
cube = power_of(3)
fourth_power = power_of(4)

# Calculate powers using the created functions
print(square(3))       # Output: 2^3 = 8
print(cube(2))         # Output: 3^2 = 9
print(fourth_power(2)) # Output: 4^2 = 16
