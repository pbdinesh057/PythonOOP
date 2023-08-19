# Purpose: Used to apply a given function to each element of an iterable and generate a new iterable with the results.
# Syntax: map(function, iterable)
# Returns: An iterator (map object) containing the results of applying the function to each element.

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]


############################################################
# List of items in a store along with their prices in rupees
store = [("Shirt", 500),
         ("Pants", 1000),
         ("Shoes", 700),
         ("Assessories", 1200)]

# Lambda function to convert rupees to dollars
to_dollar = lambda data: [(data[0], data[1] / 77)]

# Apply the to_dollar lambda function to each item in the store using map
store_dollars = map(to_dollar, store)

# Convert the map object to a list to see the results
list_sd = list(store_dollars)

# Print the items and their prices in dollars
for i in list_sd:
    print(i)
print("\n")

# Lambda function to sort items by price
sort_by_price = lambda price: price[1]

# Sort the store list by price in descending order
store.sort(key=sort_by_price, reverse=True)

# Print the sorted items and their prices
for k in store:
    print(k)


