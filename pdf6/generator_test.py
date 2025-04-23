# Generate passwords with itertools 
import itertools 
import string 
def gen_passwords(chars, length): 
    for combo in itertools.product(chars, repeat=length): 
        yield ''.join(combo) 
chars = "ab" 
for pwd in gen_passwords(chars, 2): 
    print(pwd)  # Outputs: aa, ab, ba, bb