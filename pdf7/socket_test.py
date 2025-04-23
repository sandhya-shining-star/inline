# Resolve hostname and test a port with banner 
import socket 
host = "example.com" 
port = 80  # HTTP 
ip = socket.gethostbyname(host) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(1) 
if sock.connect_ex((ip, port)) == 0: 
    banner = sock.recv(1024).decode().strip() 
    print(f"IP: {ip}, Port {port} open, Banner: {banner}") 
else: 
    print(f"Port {port} closed on {ip}") 
sock.close()