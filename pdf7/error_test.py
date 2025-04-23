# Handle socket errors 
import socket 
target = "127.0.0.1" 
port = 9999  # Unlikely to be open 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(1) 
try: 
    sock.connect_ex((target, port)) 
    banner = sock.recv(1024).decode() 
    print(f"Banner: {banner}") 
except socket.timeout: 
    print(f"Timeout on port {port}") 
except: 
    print(f"Failed to get banner on port {port}") 
sock.close()