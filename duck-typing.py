# Duck typing is a concept where the class of an object is less important than its methods/attributes.
# It focuses on behavior rather than explicit class type.

# Define classes representing different animals with common methods.
class Duck:
    def walk(self):
        print("The Duck is walking")
    def talk(self):
        print("The Duck is quacking")

class Chicken:
    def walk(self):
        print("The Chicken is walking")
    def talk(self):
        print("The Chicken is talking")

class Predator:
    def walk(self):
        print("The Predator is walking")
    def talk(self):
        print("The Predator is shouting")

# Define a Person class with a catch method that demonstrates duck typing.
class Person:
    def catch(self, bird):
        # Using duck typing, this method works with any object that has walk and talk methods.
        bird.walk()
        bird.talk()
        print("You caught the bird")

# Create instances of the different animal classes.
duck = Duck()
chicken = Chicken()
predator = Predator()
person = Person()

# Call the catch method with different objects (Duck, Chicken, Predator).
person.catch(duck)       # Duck object
person.catch(chicken)    # Chicken object
person.catch(predator)   # Predator object


###################################################################################################################
###################################################################################################################
"""
# a practical code example that demonstrates the use of duck typing in a real-world scenario. In this example, we'll implement a simple logging system that can work with different types of log sources, such as files and databases, using duck typing.
"""

class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

class DatabaseLogger:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def log(self, message):
        # Simulated database insert operation
        print(f"Inserting '{message}' into database")

def log_data(logger, data):
    logger.log(data)

# Create instances of different loggers
file_logger = FileLogger("logfile.txt")
db_logger = DatabaseLogger("my_database")

# Log data using different loggers, demonstrating duck typing
log_data(file_logger, "This is a log message from a file logger")
log_data(db_logger, "This is a log message from a database logger")

"""
##########Explanation###########
Certainly! Let's go through the provided code step by step and explain each part:

```python
class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')
```

In this part of the code, we define a class `FileLogger`. This class has two methods:

- `__init__`: The constructor method that initializes the object with a `filename` attribute.
- `log`: A method that takes a `message` as an argument and appends the message to a file specified by the `filename` attribute.

```python
class DatabaseLogger:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def log(self, message):
        # Simulated database insert operation
        print(f"Inserting '{message}' into database")
```

Similarly, we define another class `DatabaseLogger`. This class also has two methods:

- `__init__`: The constructor method that initializes the object with a `db_connection` attribute.
- `log`: A method that takes a `message` as an argument and simulates inserting the message into a database. In this example, we print a message to represent the database operation.

```python
def log_data(logger, data):
    logger.log(data)
```

Next, we define a function `log_data` that takes two arguments: a `logger` object and `data` to be logged. Inside this function, we call the `log` method of the `logger` object to log the provided data.

```python
file_logger = FileLogger("logfile.txt")
db_logger = DatabaseLogger("my_database")
```

We create instances of `FileLogger` and `DatabaseLogger` classes, passing the appropriate parameters (`filename` for `FileLogger` and `db_connection` for `DatabaseLogger`).

```python
log_data(file_logger, "This is a log message from a file logger")
log_data(db_logger, "This is a log message from a database logger")
```

Finally, we use the `log_data` function to log messages using different loggers (`file_logger` and `db_logger`). This demonstrates duck typing: the function works with both types of loggers even though they are different classes, as long as they have a compatible `log` method.

Overall, the example showcases how duck typing allows us to create a logging system that works with different logger objects, providing flexibility and code reusability.
"""