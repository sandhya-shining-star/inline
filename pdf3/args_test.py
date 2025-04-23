#Parse command-line arguments 
import argparse 

parser = argparse.ArgumentParser(description="Sample argument parser") 
parser.add_argument("name", help="Your name") 
parser.add_argument("--age", type=int, default=20, help="Your age") 
args = parser.parse_args() 
print(f"Name: {args.name}, Age: {args.age}") 