# Run a shell command 
import os  # Add this line
import subprocess 
cmd = "dir" if os.name == "nt" else "ls -l" 
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
stderr=subprocess.PIPE, universal_newlines=True) 
output = process.stdout.read() + process.stderr.read() 
print(f"Output: {output}") 