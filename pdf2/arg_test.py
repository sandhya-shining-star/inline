# Parse command-line arguments 
import sys 

if len(sys.argv) != 3: 
    print("Usage: python script.py <name> <age>") 
    sys.exit(1) 
name = sys.argv[1] 
age = sys.argv[2] 
print(f"Hello, {name}! You are {age} years old.") 