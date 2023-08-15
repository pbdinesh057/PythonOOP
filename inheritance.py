class Animal:
    alive = True
    def eat(self):
        print("This Animal can eat")
    def sleep(self):
        print("This animal can sleep")

class Rabbit(Animal):
    def run(self):
        print("Running fast")

class Fish(Animal):
    def swim(self):
        print("Swim")

class Hawk(Animal):
    def fly(self):
        print("Fly")

class Whale(Fish): #multi-level inheritance  ===== receives attributes form Fish and Animal
    def largest(self):
        print("Largest sea animal")

# Create an instance of Whale
whale_instance = Whale()

# Call the swim method on the Whale instance
whale_instance.swim()
