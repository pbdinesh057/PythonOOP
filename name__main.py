"""
The if __name__ == '__main__': construct is used for a specific purpose in Python scripts to achieve two main goals:

Module Reusability: When you write a Python script, you might create functions, classes, and other components that are meant to be reused in different scripts or projects. By using the if __name__ == '__main__': block, you can include test code, example usage, or any other code that should be executed only when the script is run directly. This allows you to keep your module's reusable components separate from the code that's specific to running the script.

Preventing Unintended Execution: Sometimes, you may write code in your script that you want to execute only when you run the script directly, not when it's imported as a module into another script. The if __name__ == '__main__': block ensures that code within this block is executed only when the script is run directly. This prevents unintended execution of certain code when the script is imported elsewhere.

"""
# module-1 code
import name__main_2

def hello():
    print("Hello")

# name__main_2.second_module()  # Comment this line

if __name__ == '__main__':
    hello()
    #name__main_2.second_module()
print(__name__)
print(name__main_2.__name__)