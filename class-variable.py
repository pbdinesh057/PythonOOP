#class variable is a variable that is shared among all instances (objects) of a class. Unlike instance variables, which have different values for each object, a class variable maintains the same value across all objects of the class. Class variables are defined within the class and are accessible through the class itself or any instance of the class.


from car import Car

print(Car.wheels)
Car.wheels = 2
print(Car.wheels)