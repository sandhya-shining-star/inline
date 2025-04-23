# Read a wordlist file 
with open("wordlist.txt", "w") as f: 
    f.write("pass1\npass2\npass3\n")  # Create sample wordlist 
with open("wordlist.txt", "r") as f: 
    passwords = [line.strip() for line in f.readlines()] 
    print("Loaded passwords:", passwords) 