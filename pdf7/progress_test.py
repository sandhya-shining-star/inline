# Dynamic progress display 
import sys 
import time 
for i in range(5):
    sys.stdout.write(f"\rProgress: {i+1}/5") 
    sys.stdout.flush() 
    time.sleep(0.5) 
print("\nDone")  