# Basic multithreading example
import threading
import time

# Define the task function
def task(name):
    print(f"Thread {name} starting")
    time.sleep(1)  # Simulate work
    print(f"Thread {name} finished")

# Create a list to hold threads
threads = []

# Start 3 threads
for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads done")
