# Compute a simple hash 
import hashlib 
password = "test123" 
hash_fn = hashlib.md5  # Example hash function 
hashed = hash_fn(password.encode()).hexdigest() 
print(f"Password: {password}, MD5 Hash: {hashed}") 