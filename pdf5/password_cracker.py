import hashlib
import itertools
import string
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Supported hash types
hash_name = ['md5', 'sha1', 'sha256', 'sha512']

# Generate passwords (for brute force)
def generate_passwords(min_length, max_length, charset):
    """
    Generates all possible combinations of passwords within a range of lengths.
    """
    for length in range(min_length, max_length + 1):
        for password in itertools.product(charset, repeat=length):
            yield ''.join(password)

# Hash a password and compare
def check_hash(password, hash_fn, target_hash):
    """
    Hashes a password with the specified hash function and compares it to the target hash.
    """
    hashed_password = hash_fn(password.encode()).hexdigest()
    return hashed_password == target_hash

# Password cracking function
def crack_hash(hash_type, target_hash, wordlist=None, min_length=1, max_length=5, charset=string.ascii_letters+string.digits):
    """
    Cracks the given hash by comparing it to potential passwords from a wordlist or generator.
    Uses multithreading for efficiency.
    """
    # Validate hash type
    if hash_type not in hash_name:
        print(f"Error: Unsupported hash type '{hash_type}'.")
        return
    
    # Hash function based on hash type
    hash_fn = getattr(hashlib, hash_type)

    # Create password source (wordlist or generated passwords)
    if wordlist:
        try:
            with open(wordlist, 'r') as file:
                passwords = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: Wordlist file '{wordlist}' not found.")
            return
    else:
        passwords = generate_passwords(min_length, max_length, charset)
    
    # Multithreaded password testing
    with ThreadPoolExecutor() as executor:
        futures = []
        progress = tqdm(total=len(passwords) if isinstance(passwords, list) else None, desc="Cracking", unit="password")

        for password in passwords:
            futures.append(executor.submit(check_hash, password, hash_fn, target_hash))
            progress.update(1)

            # Check results
            for future in futures:
                if future.result():
                    progress.close()
                    print(f"Password found: {password}")
                    return

    progress.close()
    print("No matching password found.")

# Argument parsing
def main():
    """
    Parse command-line arguments and run the password cracker.
    """
    parser = argparse.ArgumentParser(description="Password Cracker")
    parser.add_argument("hash", help="Target hash to crack")
    parser.add_argument("--hash_type", choices=hash_name, required=True, help="Hash type (e.g., md5, sha1, sha256, sha512)")
    parser.add_argument("--wordlist", help="Path to wordlist file")
    parser.add_argument("--min_length", type=int, default=1, help="Minimum password length (for brute-force)")
    parser.add_argument("--max_length", type=int, default=5, help="Maximum password length (for brute-force)")
    parser.add_argument("--charset", default=string.ascii_letters+string.digits, help="Character set for brute-force")
    args = parser.parse_args()

    # Run the cracking function
    crack_hash(args.hash_type, args.hash, args.wordlist, args.min_length, args.max_length, args.charset)

if __name__ == "__main__":
    main()
