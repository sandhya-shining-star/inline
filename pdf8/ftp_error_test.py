# Handle FTP login errors 
import ftplib 
host = "127.0.0.1" 
user = "testuser" 
password = "wrong" 
try: 
    with ftplib.FTP() as server: 
        server.connect(host, 21, timeout=1) 
        server.login(user, password) 
        print("Success") 
except ftplib.error_perm: 
    print("Authentication failed") 
except Exception as e: 
    print(f"Error: {e}") 