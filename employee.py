class Employee:
    # Class variable to keep track of the number of employees
    total_employees = 0 #class variables

    def __init__(self, name, salary):
        self.name = name #instance variables
        self.salary = salary
        # Increment the class variable when a new employee is created
        Employee.total_employees += 1