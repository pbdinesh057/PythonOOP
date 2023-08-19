# creates a dictionaries using an expression || can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable if conditional}
# dictionary = {key: function(value) for (key,value) in iterable if conditional}


# Creating a dictionary using dictionary comprehension to convert temperatures from Fahrenheit to Celsius
cities_in_F = {"NewYork": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# Filtering cities with "Sunny" weather using dictionary comprehension
cities_weather = {"NewYork": "Sunny", "Boston": "Sunny", "Los Angeles": "Cloudy", "Chicago": "Windy"}
cities_Sunny = {key: value for (key, value) in cities_weather.items() if value == "Sunny"}
print(cities_Sunny)

# Creating a dictionary with descriptions of cities based on temperature using dictionary comprehension
cities = {"NewYork": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
description_of_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(description_of_cities)

# Defining a function to check temperature categories
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

# Using the function within dictionary comprehension to describe cities based on temperature
cities = {"NewYork": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_city = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_city)
