import requests
import threading

# Setup
domain = 'youtube.com'  # Target domain
discovered_subdomains = []  # List to store discovered subdomains
lock = threading.Lock()  # Lock for thread-safe operations

# Read Subdomains
try:
    with open('test_subdomains.txt') as file:  # Updated file name
        subdomains = file.read().splitlines()  # Load subdomains as a list
except FileNotFoundError:
    print("[!] Error: The file 'test_subdomains.txt' was not found. Please create it and add subdomains.")
    exit()

# Define the Check Function
def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'  # Construct the subdomain URL
    try:
        response = requests.get(url, timeout=5)  # Attempt HTTP GET request with a 5-second timeout
        if response.status_code == 200:  # If the subdomain is reachable
            print(f"[+] Found subdomain: {url}")
            with lock:  # Ensure thread-safe operation
                discovered_subdomains.append(url)
    except requests.ConnectionError:
        print(f"[-] Connection error for {url}")
    except requests.Timeout:
        print(f"[-] Timeout for {url}")
    except requests.RequestException as e:
        print(f"[!] An error occurred for {url}: {e}")

# Launch Threads
threads = []
for sub in subdomains:
    t = threading.Thread(target=check_subdomain, args=(sub,))
    t.start()
    threads.append(t)

# Wait and Save
for t in threads:
    t.join()  # Wait for all threads to finish

# Save discovered subdomains to a file
if discovered_subdomains:
    with open('discovered_subdomains.txt', 'w') as file:
        for subdomain in discovered_subdomains:
            file.write(subdomain + '\n')
    print("[*] Subdomain discovery complete. Results saved to 'discovered_subdomains.txt'")
else:
    print("[!] No subdomains were discovered.")
