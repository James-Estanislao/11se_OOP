import threading
import time

def loop_one():
    while True:
        print("Loop 1 is running...")
        time.sleep(1)
        
def loop_two():
    while True:
        print("Loop 2 is running...")
        time.sleep(1.5)
        

# Assign functions to separate threads
thread1 = threading.Thread(target=loop_one)
thread2 = threading.Thread(target=loop_two)

# Start execution
thread1.start()
thread2.start()
