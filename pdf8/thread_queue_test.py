# Use threads and a queue 
import threading 
import queue 
import time 
q = queue.Queue() 
def worker(): 
    while not q.empty(): 
        task = q.get() 
        print(f"Processing: {task}") 
        time.sleep(0.5) 
        q.task_done() 
for i in range(3): 
    q.put(f"Task {i}") 
threads = [threading.Thread(target=worker, daemon=True) for _ in 
range(2)] 
for t in threads: 
    t.start() 
q.join() 
print("All tasks done") 