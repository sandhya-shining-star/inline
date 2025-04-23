import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from colorama import Fore, Style

# ANSI color codes
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

def scan_port(host, port):
    """
    Scan a single port to check if it's open, identify services, and grab banners.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            # Connect to the port
            if s.connect_ex((host, port)) == 0:
                try:
                    # Get service name
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown Service"
                
                # Attempt to retrieve banner
                try:
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No Banner"
                
                return f"{GREEN}Port {port}: OPEN | Service: {service} | Banner: {banner}{RESET}"
            else:
                return None
    except Exception as e:
        return f"{RED}Error scanning port {port}: {e}{RESET}"

def format_port_results(results):
    """
    Format scan results into a table.
    """
    print(f"\n{CYAN}Scan Results:{RESET}")
    for result in results:
        if result:  # Only display open ports
            print(result)

def port_scan(host, port_range):
    """
    Resolve hostname, scan ports in parallel, and display results.
    """
    try:
        # Resolve hostname to IP
        ip = socket.gethostbyname(host)
        print(f"{CYAN}Scanning Host: {host} (IP: {ip}){RESET}\n")
    except socket.gaierror:
        print(f"{RED}Unable to resolve hostname: {host}{RESET}")
        sys.exit(1)

    results = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Create future tasks for each port in the range
        futures = [executor.submit(scan_port, ip, port) for port in port_range]
        for future in as_completed(futures):
            results.append(future.result())

    format_port_results(results)

if __name__ == "__main__":
    # Entry point: Get user input for target hostname and port range
    try:
        target = input(f"{CYAN}Enter target hostname: {RESET}")
        start_port = int(input(f"{CYAN}Enter starting port: {RESET}"))
        end_port = int(input(f"{CYAN}Enter ending port: {RESET}"))

        # Validate port range
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print(f"{RED}Invalid port range!{RESET}")
            sys.exit(1)

        port_range = range(start_port, end_port + 1)
        port_scan(target, port_range)

    except ValueError:
        print(f"{RED}Invalid input! Please provide numeric values for ports.{RESET}")
        sys.exit(1)
