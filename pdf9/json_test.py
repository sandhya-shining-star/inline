# JSON encode and decode 
import json 
data = {"command": "dir"} 
json_data = json.dumps(data) 
print(f"Encoded: {json_data}") 
decoded = json.loads(json_data)
print(f"Decoded: {decoded}")