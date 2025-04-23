# Read a wordlist file 
with open("test_pass.txt", "w") as f: 
    f.write("pass1\npass2\npass3\n")  # Create sample wordlist 
with open("test_pass.txt", "r") as f: 
    passwords = f.read().splitlines() 
print("Passwords:", passwords) 