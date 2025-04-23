# Use threads and a queue 
import threading 
from queue import Queue 
import time 
def worker(num, q): 
    time.sleep(1)
    q.put(f"Worker {num} done") 
q = Queue() 
threads = [] 
for i in range(3): 
    t = threading.Thread(target=worker, args=(i, q)) 
    t.start() 
    threads.append(t) 
for t in threads: 
    t.join() 
while not q.empty(): 
    print(q.get()) 
