# Function with multiple arguments 
def combine_files(file1, file2, output): 
    with open(file1, "r") as f1, open(file2, "r") as f2: 
        content = f1.read() + f2.read() 
        with open(output, "w") as out: 
            out.write(content) 
            print(f"Combined {file1} and {file2} into {output}") 
combine_files("file1.txt", "file2.txt", "combined.txt")