# Use ThreadPoolExecutor for parallel tasks 
from concurrent.futures import ThreadPoolExecutor 
import time 
def task(n): 
    time.sleep(0.5) 
    return f"Task {n} done" 
with ThreadPoolExecutor(max_workers=2) as executor: 
    futures = [executor.submit(task, i) for i in range(4)] 
    for future in futures: 
        print(future.result()) 