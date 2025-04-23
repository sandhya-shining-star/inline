# Use string module for character sets 
import string 
chars = string.ascii_letters + string.digits 
print(f"Character set: {chars[:20]}... (total {len(chars)})") 