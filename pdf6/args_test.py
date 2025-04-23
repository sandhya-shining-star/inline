# Parse command-line arguments 
import argparse 
parser = argparse.ArgumentParser(description="Test parser") 
parser.add_argument("target", help="Target host") 
parser.add_argument("-u", "--user", help="Username") 
parser.add_argument("--retry", action="store_true", help="Enable retries") 
args = parser.parse_args() 
print(f"Target: {args.target}, User: {args.user}, Retry: {args.retry}") 
