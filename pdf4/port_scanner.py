import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Scans a single port on the target IP address.
    Tries to establish a socket connection and retrieve the banner.
    """
    try:
        # Create a socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for connection
            # Attempt to connect to the port
            if s.connect_ex((ip, port)) == 0:  # Successful connection
                try:
                    # Attempt banner grabbing
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                print(f"Port {port}: OPEN - {banner}")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    """
    Main function to handle user input and initiate port scanning.
    """
    # Get target IP and port range from user
    ip = input("Enter the target IP address: ")
    port_range = input("Enter the port range (e.g., 1-100): ").split('-')
    start_port, end_port = int(port_range[0]), int(port_range[1])

    print(f"\nScanning {ip} for open ports...\n")

    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    main()
