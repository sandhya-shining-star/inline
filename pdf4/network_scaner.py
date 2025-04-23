import scapy.all as scapy
import threading
from queue import Queue
import socket
import ipaddress

# Function to send ARP requests and process responses
def scan(ip, result_queue):
    """
    Sends an ARP request to the specified IP address.
    Stores the response in the result queue if the device is active.
    """
    try:
        # Create an ARP request packet
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast / arp_request
        # Send the packet and capture responses
        answered = scapy.srp(packet, timeout=1, verbose=False)[0]

        for send, receive in answered:
            # Extract IP and MAC addresses
            client = {'IP': receive.psrc, 'MAC': receive.hwsrc}
            try:
                # Perform reverse DNS lookup to resolve hostname
                client['Hostname'] = socket.gethostbyaddr(receive.psrc)[0]
            except socket.herror:
                client['Hostname'] = "Unknown"
            result_queue.put(client)
    except Exception as e:
        print(f"An error occurred while scanning {ip}: {e}")

# Function to print the results
def print_results(results):
    """
    Displays the scan results in a table format.
    """
    print(f"\n{'IP Address':<20}{'MAC Address':<20}{'Hostname':<30}")
    print('-' * 70)
    for result in results:
        print(f"{result['IP']:<20}{result['MAC']:<20}{result['Hostname']:<30}")

# Main function to manage the scanning process
def main():
    """
    Main function to accept user input and coordinate the network scan.
    """
    # Prompt the user for the target network
    cidr = input("Enter CIDR range (e.g., 192.168.1.0/24): ")
    try:
        # Validate and generate IP addresses from the CIDR range
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        print("Invalid CIDR range. Please try again.")
        return

    # Prepare threads and a queue for storing results
    threads = []
    result_queue = Queue()

    print(f"\nScanning the network: {cidr}...\n")

    # Spawn threads for each IP in the network
    for ip in network.hosts():
        thread = threading.Thread(target=scan, args=(str(ip), result_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Collect all results from the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Print results
    if results:
        print_results(results)
    else:
        print("No active devices found on the network.")

if __name__ == "__main__":
    main()
