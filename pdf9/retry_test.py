# Retry on connection failure 
import socket 
import time 
def connect_with_retry(ip, port): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    while True: 
        try: 
            s.connect((ip, port)) 
            print("Connected") 
            break 
        except ConnectionRefusedError: 
            print("Connection failed, retrying...") 
            time.sleep(1) 
    s.close() 
connect_with_retry("127.0.0.1", 9999)  # No server running 