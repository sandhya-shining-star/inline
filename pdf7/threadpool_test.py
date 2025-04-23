from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def task(n):
    time.sleep(0.5)  # Simulate work
    return f"Task {n} done"

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(task, i) for i in range(4)]
    for future in as_completed(futures):  # Use as_completed from concurrent.futures
        print(future.result())
