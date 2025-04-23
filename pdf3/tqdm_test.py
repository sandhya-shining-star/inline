# Display a progress bar with tqdm 
from tqdm import tqdm 
import time 
for i in tqdm(range(5), desc="Processing", unit="step"): 
    time.sleep(0.5)  # Simulate work 
print("Done!")