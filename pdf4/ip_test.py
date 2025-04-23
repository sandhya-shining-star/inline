#Parse CIDR and list host IPs 
import ipaddress 
cidr = "192.168.1.0/24" 
network = ipaddress.ip_network(cidr, strict=False) 
for ip in list(network.hosts())[:5]:   
    print(f"Host IP: {ip}") 