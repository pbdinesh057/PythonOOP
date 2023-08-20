# daemon thread = a thread that runs in the background, not important for program to run
                # tasks that don't need to be completed before the program exits
                # automatically terminated when the main program (or the last non-daemon thread) exits,

# your program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normally be killed, stays alive until task is completed
# eg - bg tasks, garbage collection, waiting for input, long running processes


import threading
import time

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for:", count, "seconds")

# Create a daemon thread for the timer function
x = threading.Thread(target=timer, daemon=True)
x.start()

# Ask the user for input
answer = input("Do you wish to exit?\n")
# The input will be handled by the Main thread, and the daemon thread will continue running

# Since the daemon thread is set to daemon=True, it will automatically be terminated when the Main thread exits.
# This happens regardless of whether the daemon thread has finished its task or not.
