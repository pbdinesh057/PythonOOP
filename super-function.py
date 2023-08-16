# super() = Function used to give access to methods of a parent class
#           Returns a temporary object of a parent class when used

# Define a parent class 'Rectangle' with attributes 'length' and 'width'
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


# Define a subclass 'Square' that inherits from 'Rectangle'
class Square(Rectangle):
    def __init__(self, length, width):
        # Call the parent class's __init__ method using 'super()'
        super().__init__(length, width)

    def area(self):
        # Calculate the area of the square (length * width)
        return self.length * self.width


# Define another subclass 'Cube' that inherits from 'Rectangle'
class Cube(Rectangle):
    def __init__(self, length, width, height):
        # Call the parent class's __init__ method using 'super()'
        super().__init__(length, width)
        self.height = height

    def volume(self):
        # Calculate the volume of the cube (length * width * height)
        return self.length * self.width * self.height


# Create an instance of the 'Square' class with dimensions 4x4
square_instance = Square(4, 4)

# Create an instance of the 'Cube' class with dimensions 6x6x6
cube_instance = Cube(6, 6, 6)

# Calculate and print the area of the square
print("Area of the square:", square_instance.area())

# Calculate and print the volume of the cube
print("Volume of the cube:", cube_instance.volume())


##################################################################

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return super().display_info() + f", {self.num_doors}-door"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def display_info(self):
        return super().display_info() + f", {self.engine_size}cc engine"

# Create instances of different types of vehicles
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 883)

# Display information about the vehicles
print(car.display_info())
print(motorcycle.display_info())


#################################################################################################################

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the __init__ method of the parent class
        self.age = age

    def greet(self):  # Override the greet method
        return f"Hi, I am {self.name} and I am {self.age} years old"

# Create an instance of the Child class
child = Child("Dinesh", 24)

# Call the overridden greet method of the Child class
print(child.greet())  # Output: Hi, I am Alice and I am 5 years old

# Access the parent class's greet method using super()
parent_greeting = super(Child, child).greet()
print(parent_greeting)  # Output: Hello, I am Alice
