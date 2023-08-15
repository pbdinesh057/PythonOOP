from employee import Employee

# Create instances of the Employee class
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
employee3 = Employee("Dinesh", 1000000)
# employee4 = Employee("C",1)

# Access the class variable using the class itself
print("Total employees:", Employee.total_employees)

# Access the class variable using an instance
print("Total employees (via instance):", employee1.total_employees)