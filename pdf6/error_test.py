# Handle SSH connection errors 
import socket 
import paramiko 
host = "127.0.0.1" 
user = "testuser" 
password = "wrong" 
client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
try: 
    client.connect(hostname=host, username=user, password=password, timeout=1) 
    print("Success") 
except socket.timeout: 
    print("Timeout error") 
except paramiko.AuthenticationException: 
    print("Authentication failed") 
except paramiko.SSHException as e: 
    print(f"SSH error: {e}") 
client.close()