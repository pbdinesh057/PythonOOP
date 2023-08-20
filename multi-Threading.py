# Thread = Flow of execution. like a separate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL = Global Interpreter Lock - allows only 1 thread to hold control of the python interpreter


# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive) - use multiprocessing

# IO bound = program/task spends most of it's time waiting for external events (user input, web scraping) - use multithreading (Quiz game - user input thread and alternate timer thread)

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you ate breakfast")
def drink_coffee():
    time.sleep(4)
    print("you drank coffee")
def study():
    time.sleep(5)
    print("you are studying")
def get_ready():
    time.sleep(9)
    print("Getting ready")

# below functions takes 12 secs to complete, instead we can use multi-threading to run at a time
# eat_breakfast()
# drink_coffee()
# study()

# Making 3 functions run concurrently, creating 3 additional threads

# Creating threads for each function to run concurrently
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
a = threading.Thread(target=get_ready, args=())
a.start()

# Waiting for all threads to finish before continuing
x.join()
y.join()
z.join()
a.join()

# Print the number of active threads
print("Number of active threads:", threading.activeCount())

# Print the list of all active threads
print("List of active threads:", threading.enumerate())

# Print the current time in seconds since the epoch
print("Current time:", time.perf_counter())
