# Define a class named "Car"
class Car:
    # The __init__ method is the constructor that initializes object attributes
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Method to simulate driving the car
    def drive(self):
        print("This " + self.model + " is driving")

    # Method to simulate stopping the car
    def stop(self):
        print("This " + self.model + " is stopped")