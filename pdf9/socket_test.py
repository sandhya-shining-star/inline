import socket
import threading
import time

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 4444))
    s.listen(1)
    print("Server listening on port 4444...")
    
    conn, addr = s.accept()
    print(f"Connected from {addr}")
    conn.close()

def client():
    time.sleep(1)  # Ensures the server is ready before the client tries to connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4444))
    print("Connected to server")
    s.close()

# Start the server in a separate thread
server_thread = threading.Thread(target=server, daemon=True)  
server_thread.start()

# Run the client
client()

# Wait for the server thread to complete
server_thread.join()
