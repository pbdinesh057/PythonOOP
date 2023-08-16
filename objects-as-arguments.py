# Define a class 'car'
class Car:
    color = None

# Define another class 'MotorCycle'
class MotorCycle:
    color = None

# Define a function to change the color of a vehicle
def change_color(vehicle, color):
    # Set the 'color' attribute of the passed vehicle object
    vehicle.color = color

# Create instances of the classes
car_1 = Car()
car_2 = Car()
bike_1 = MotorCycle()

# Call the 'change_color' function to change the color of each vehicle
change_color(car_1, "white")  # Change color of car_1 to white
change_color(car_2, "Black")  # Change color of car_2 to black
change_color(bike_1, "Red")   # Change color of bike_1 to red

# Print the color attribute of each vehicle
print(car_1.color)  # Output: white
print(car_2.color)  # Output: Black
print(bike_1.color) # Output: Red
#######################################################################################

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def update_age(student_obj, new_age):
    student_obj.age = new_age

# Create instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Print the initial ages
print("Initial Ages:")
print(student1.name, ":", student1.age)
print(student2.name, ":", student2.age)

# Call the update_age function to change the ages
update_age(student1, 21)
update_age(student2, 23)

# Print the updated ages
print("\nUpdated Ages:")
print(student1.name, ":", student1.age)
print(student2.name, ":", student2.age)
