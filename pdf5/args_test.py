# Parse command-line arguments 
import argparse 
parser = argparse.ArgumentParser(description="Test parser") 
parser.add_argument("input", help="Input string") 
parser.add_argument("--option", default="default", help="Optional value") 
args = parser.parse_args() 
print(f"Input: {args.input}, Option: {args.option}")