# Send and receive data over sockets 
import socket 
import threading 
def server(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind(("127.0.0.1", 4444)) 
    s.listen(1) 
    conn, _ = s.accept() 
    conn.send("Hello from server".encode())
    conn.close() 
def client(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(("127.0.0.1", 4444)) 
    data = s.recv(1024).decode() 
    print(f"Received: {data}") 
    s.close() 
t = threading.Thread(target=server) 
t.start() 
client() 
t.join()