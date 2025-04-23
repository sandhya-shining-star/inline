# Copy a file in binary mode 
input_file = "test.txt" 
output_file = "test_copy.txt" 
with open(input_file, "wb") as f: 
    f.write(b"Sample text")  # Write sample data 
with open(input_file, "rb") as source: 
    data = source.read() 
with open(output_file, "wb") as dest: 
    dest.write(data) 
print(f"Copied {input_file} to {output_file}")