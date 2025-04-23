import requests
import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

# ANSI color codes
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

def check_subdomain(domain, subdomain):
    """
    Check if a subdomain is active by sending an HTTP request.
    """
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"{GREEN}[ACTIVE]{RESET} {url}")
            return url
    except requests.ConnectionError:
        pass
    except requests.exceptions.RequestException as e:
        print(f"{RED}[ERROR]{RESET} {url} - {e}")
    return None

def save_results(active_subdomains):
    """
    Save discovered subdomains to an output file.
    """
    with open("discovered_subdomains.txt", "w") as file:
        for subdomain in active_subdomains:
            file.write(f"{subdomain}\n")
    print(f"{CYAN}Discovered subdomains saved to discovered_subdomains.txt{RESET}")

def subdomain_enum(domain, subdomains_file):
    """
    Main function to perform subdomain enumeration.
    """
    try:
        # Load subdomains from the file
        with open(subdomains_file, "r") as file:
            subdomains = file.read().splitlines()
        print(f"{CYAN}Loaded {len(subdomains)} subdomains to scan.{RESET}")
    except FileNotFoundError:
        print(f"{RED}File not found: {subdomains_file}{RESET}")
        return

    active_subdomains = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_subdomain, domain, subdomain) for subdomain in subdomains]
        for future in futures:
            result = future.result()
            if result:
                active_subdomains.append(result)

    save_results(active_subdomains)

if __name__ == "__main__":
    # Prompt user for inputs
    domain = input(f"{CYAN}Enter target domain: {RESET}")
    subdomains_file = input(f"{CYAN}Enter subdomains file path: {RESET}")
    subdomain_enum(domain, subdomains_file)
