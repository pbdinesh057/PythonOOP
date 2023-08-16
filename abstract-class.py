"""
1. abstract class = a class which contains one or more abstract methods
2. abstract method = a method that has a declaration but no implementation
3. abstract class prevent a user from creating an object from that class, since it's just a blueprint
4. compels a user to override abstract methods in a child class
5. abstract class methods may be empty, but if any class inherits this abstract class, they must follow the blueprint     which was declared under @abstractmethod, like defining same function without deviation.
6. child class must define all methods which are in main abstract class(may be some extra methods too), but shouldn't     miss any from main class
"""

# Import the ABC (Abstract Base Class) module and the abstractmethod decorator
from abc import ABC, abstractmethod

# Define an abstract class 'Vehicle'
class Vehicle(ABC):

    # Define abstract methods 'go' and 'stop'
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Define a concrete class 'Car' that inherits from 'Vehicle'
class Car(Vehicle):

    # Implement the 'go' method for 'Car'
    def go(self):
        print("Car is Running")

    # Implement the 'stop' method for 'Car'
    def stop(self):
        print("This CAR will stop")

# Define another concrete class 'Motorcycle' that inherits from 'Vehicle'
class Motorcycle(Vehicle):

    # Implement the 'go' method for 'Motorcycle'
    def go(self):
        print("Motorcycle is driving")

    # Implement the 'stop' method for 'Motorcycle'
    def stop(self):
        print("This MC will stop")

    # Define an additional method 'run' for 'Motorcycle'
    def run(self):
        print("THIS WILL RUN")

# Create instances of the concrete classes
car = Car()
mc = Motorcycle()

# Call methods on the instances
car.go()      # Output: Car is Running
car.stop()    # Output: This CAR will stop
mc.go()       # Output: Motorcycle is driving
mc.stop()     # Output: This MC will stop
mc.run()      # Output: THIS WILL RUN


######################################################################

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):  # An additional method specific to Circle
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating instances of subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling methods on subclasses
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 31.400000000000002
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24



