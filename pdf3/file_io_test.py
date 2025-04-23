# Read a wordlist file line-by-line 
wordlist = "passwords.txt" 
# Create a sample wordlist 
with open(wordlist, "w") as f: 
    f.write("pass1\npass2\npass3\n") 
# Read it back 
with open(wordlist, "r") as f: 
    passwords = [line.strip() for line in f] 
    print("Passwords loaded:", passwords) 