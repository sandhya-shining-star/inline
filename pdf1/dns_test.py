import socket 
domain = "youtube.com" 
try: 
    ip = socket.gethostbyname(domain)  # Make sure this line is indented
    print(f"IP address of {domain}: {ip}") 
except socket.gaierror: 
    print(f"Could not resolve {domain}")  # Indent this as well
