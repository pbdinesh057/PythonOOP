# Method overriding is a fundamental concept in object-oriented programming (OOP) that allows a subclass to provide a specific implementation for a method that it inherits from its parent class. When a method is overridden in a subclass, the subclass version of the method takes precedence over the version inherited from the parent class.

# Define the 'animal' class with a method 'eat'
class Animal:
    def eat(self):
        print("This Animal eats")

# Define the 'rabbit' class inheriting from 'Animal'
class Rabbit(Animal):
    # Override the 'eat' method in the subclass
    def eat(self):
        print("Rabbits eat carrots")

# Create an instance of the 'rabbit' class
rabbit_instance = Rabbit()

# Call the overridden 'eat' method on the 'rabbit' instance
rabbit_instance.eat()  # Outputs: Rabbits eat carrots

#####################################2nd example###########################################

class Shape:
    def area(self):
        print("Calculating area of a shape")

class Circle(Shape):
    def area(self):
        radius = 5
        calculated_area = 3.14 * radius * radius
        print(f"Calculating area of a circle: {calculated_area}")

# Create an instance of the Circle class
circle_instance = Circle()

# Call the overridden 'area' method on the Circle instance
circle_instance.area()  # Outputs: Calculating area of a circle: 78.5
