# Basic SSH connection with pxssh 
from pexpect import pxssh 
host = "127.0.0.1"  # Replace with your SSH server 
user = "testuser"   # Replace with valid user 
password = "test"   # Replace with valid password 
try: 
s = pxssh.pxssh() 
s.login(host, user, password, port=22) 
print(f"Connected to {host}") 
s.logout() 
except Exception as e: 
print(f"Error: {e}") 