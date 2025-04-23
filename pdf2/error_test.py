# Handle file-related errors 
def read_file(filename): 
    try: 
        with open(filename, "r") as f: 
            print(f.read()) 
    except FileNotFoundError: 
                print(f"Error: {filename} not found") 
    except Exception as e: 
                    print(f"Unexpected error: {e}") 
read_file("nonexistent.txt") 