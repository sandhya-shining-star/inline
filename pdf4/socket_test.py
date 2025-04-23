# Handle socket errors 
import socket 
ip = "192.168.56.1"  # Replace with a local IP 
try: 
    hostname = socket.gethostbyaddr(ip)[0] 
    print(f"Hostname: {hostname}") 
except socket.herror: 
    print(f"Hostname for {ip}: Unknown")