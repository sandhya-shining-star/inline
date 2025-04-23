# Show progress with tqdm 
from tqdm import tqdm 
import time 
for i in tqdm(range(5), desc="Processing"): 
    time.sleep(0.5) 
print("Done")