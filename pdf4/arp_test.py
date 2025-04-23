# Simple ARP request with scapy (requires root/admin privileges) 
import scapy.all as scapy 
ip = "192.168.56.1"  # Replace with a local IP 
arp = scapy.ARP(pdst=ip) 
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
packet = broadcast / arp 
result = scapy.srp(packet, timeout=1, verbose=False)[0] 
if result: 
    print(f"IP: {result[0][1].psrc}, MAC: {result[0][1].hwsrc}") 
else: 
    print(f"No response from {ip}")