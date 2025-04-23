 # Read and write a list to/from a file 
subdomains = ["www", "mail", "api"] 

# Write to a file 
with open("test_subdomains.txt", "w") as f: 
    for sub in subdomains:  # Properly indented
        print(sub, file=f)  # Properly indented

# Read from the file 
with open("test_subdomains.txt") as f: 
    loaded_subdomains = f.read().splitlines() 
    print("Loaded subdomains:", loaded_subdomains)  # Properly indented
