# Check if a single port is open 
import socket 
target = "127.0.0.1"  # Localhost 
port = 22  # SSH port 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(1) 
result = sock.connect_ex((target, port)) 
if result == 0: 
    print(f"Port {port} is open") 
else: 
    print(f"Port {port} is closed") 
sock.close() 