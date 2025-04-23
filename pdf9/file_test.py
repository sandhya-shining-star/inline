# Change directory and read/write a file 
import os 
# Change directory 
os.chdir(os.path.expanduser("~"))  # Home directory 
print(f"Current directory: {os.getcwd()}") 
# Write and read a file 
with open("test.txt", "wb") as f: 
    f.write(b"Test data") 
with open("test.txt", "rb") as f: 
    print(f"File content: {f.read()}")