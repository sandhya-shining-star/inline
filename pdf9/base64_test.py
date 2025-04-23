# Encode and decode with base64 
import base64 
data = b"Test file content" 
encoded = base64.b64encode(data).decode("utf-8") 
print(f"Encoded: {encoded}") 
decoded = base64.b64decode(encoded) 
print(f"Decoded: {decoded}")