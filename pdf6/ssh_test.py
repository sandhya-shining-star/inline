# Basic SSH connection test with paramiko 
import paramiko 
host = "127.0.0.1"  # Localhost 
user = "root"   # Replace with a valid user 
password = "toor"  # Replace with a test password 
client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
try: 
    client.connect(hostname=host, username=user, password=password, timeout=3) 
    print(f"Connected to {host} with {user}:{password}") 
except paramiko.AuthenticationException: 
    print(f"Failed login for {user}:{password}") 
client.close()