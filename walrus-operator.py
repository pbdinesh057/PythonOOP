# assignment exp
# assigns values to variables as part of larger expression
# shortens code

foods = list()
while True:
    food = input("enter Fav food: ")
    if food == "quit":
        break
    foods.append(food)

#walrus operator

foods2 = list()

while food1 := input("Enter Fav Food: ") != "quit":
    foods2.append(food1)