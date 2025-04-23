# Basic FTP connection test 
import ftplib 
host = "127.0.0.1"  # Localhost 
user = "kali"   # Replace with a valid user 
password = "root"  # Replace with a test password 
try: 
    with ftplib.FTP() as server: 
        server.connect(host, 21, timeout=5) 
        server.login(user, password) 
        print(f"Connected to {host} with {user}:{password}") 
except ftplib.error_perm: 
    print(f"Failed login for {user}:{password}") 