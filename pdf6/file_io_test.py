# Read and write a file 
with open("test_pass.txt", "w") as f: 
    f.write("pass1\npass2\npass3\n")  # Create sample password list 
with open("test_pass.txt", "r") as f: 
    passwords = f.read().splitlines() 
    print("Passwords:", passwords) 
with open("output.txt", "w") as f: 
    f.write("testuser@localhost:pass1") 
    print("Wrote to output.txt")