# Define the 'prey' class with a method 'flees'
class Prey:
    def flees(self):
        print("This animal flees or runs away")

# Define the 'Predator' class with a method 'hunt'
class Predator:
    def hunt(self):
        print("This animal hunts")

# Define the 'rabbit' class inheriting from 'Prey'
class Rabbit(Prey):
    def runs(self):
        print("This runs really fast")

# Define the 'Hawk' class inheriting from 'Predator'
class Hawk(Predator):
    def fly(self):
        print("This Flies high in the sky")

# Define the 'fish' class inheriting from both 'Prey' and 'Predator'
class Fish(Prey, Predator):
    def swim(self):
        print("This has swim ability")

# Create instances of the classes
rabbit_instance = Rabbit()
hawk_instance = Hawk()
fish_instance = Fish()

# Call methods on instances
rabbit_instance.flees()  # Outputs: This animal flees or runs away
rabbit_instance.runs()   # Outputs: This runs really fast

hawk_instance.hunt()     # Outputs: This animal hunts
hawk_instance.fly()      # Outputs: This Flies high in the sky

fish_instance.flees()    # Outputs: This animal flees or runs away
fish_instance.hunt()     # Outputs: This animal hunts
fish_instance.swim()     # Outputs: This has swim ability
