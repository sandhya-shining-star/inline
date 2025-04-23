import pikepdf
from tqdm import tqdm
import itertools
import string
import concurrent.futures
import argparse

# Function to generate passwords (example: combinations of letters)
def generate_passwords(length=4):
    chars = string.ascii_letters + string.digits
    for password in itertools.product(chars, repeat=length):
        yield ''.join(password)

# Function to load passwords from a wordlist file
def load_passwords(wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            yield line.strip()

# Function to try a password
def try_password(pdf_file, password):
    try:
        with pikepdf.open(pdf_file, password=password):
            return password  # Return the correct password if successful
    except pikepdf._core.PasswordError:
        return None  # Return None if the password fails

# Function to decrypt the PDF using multiple threads
def decrypt_pdf(pdf_file, passwords):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks and track progress with tqdm
        future_to_password = {
            executor.submit(try_password, pdf_file, password): password
            for password in passwords
        }
        for future in tqdm(concurrent.futures.as_completed(future_to_password), desc="Cracking", unit="password"):
            result = future.result()
            if result:
                return result  # Return the first successful password
    return None  # Return None if no passwords work

# Main function to handle arguments and run the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Cracker Script")
    parser.add_argument("pdf_file", help="Path to the password-protected PDF file")
    parser.add_argument("--wordlist", help="Path to the wordlist file")
    parser.add_argument("--generate", type=int, help="Length of generated passwords")
    args = parser.parse_args()

    if args.wordlist:
        passwords = load_passwords(args.wordlist)
    elif args.generate:
        passwords = generate_passwords(args.generate)
    else:
        print("Please provide either --wordlist or --generate.")
        exit(1)

    # Attempt to decrypt the PDF
    correct_password = decrypt_pdf(args.pdf_file, passwords)
    if correct_password:
        print(f"Password found: {correct_password}")
    else:
        print("Password not found.")
