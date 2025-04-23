# Use ThreadPoolExecutor for parallel tasks 
from concurrent.futures import ThreadPoolExecutor 
import time 
def slow_task(n): 
    time.sleep(1)  # Simulate work 
    return f"Task {n} done" 
with ThreadPoolExecutor(max_workers=2) as executor: 
    futures = [executor.submit(slow_task, i) for i in range(4)] 
    for future in futures: 
        print(future.result()) 
