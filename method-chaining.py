# Method Chainig is caling multiple methods sequentially.
# Each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("This will Turn-On")
        return self
    def move(self):
        print("Lets drive!!!")
        return self
    def brake(self):
        print("Apply the brakes to stop")
        return self
    def turn_off(self):
        print("This will turn-off the car")
        return self

car_inst = Car()

car_inst.turn_on()\
    .move()\
    .brake()\
    .turn_off()
#######################################################################################

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        self.value /= num
        return self


# Create an instance of the Calculator class
calc = Calculator()

# Use method chaining to perform calculations
calcs = calc.add(10).multiply(2).subtract(5).divide(3)
result = calcs.value


print("Final result:", result)  # Outputs: Final result: 5.0

