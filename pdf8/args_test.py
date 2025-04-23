# Parse command-line arguments 
import argparse 
parser = argparse.ArgumentParser(description="Test parser") 
parser.add_argument("--host", required=True, help="Target host") 
parser.add_argument("--port", type=int, default=21, help="Port") 
parser.add_argument("-t", "--threads", type=int, default=2, 
help="Threads") 
args = parser.parse_args() 
print(f"Host: {args.host}, Port: {args.port}, Threads: {args.threads}") 