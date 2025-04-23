# Generate passwords with itertools and yield 
import itertools 
def generate_words(chars, length): 
    for combo in itertools.product(chars, repeat=length): 
        yield ''.join(combo) 
chars = "ab" 
for word in generate_words(chars, 2): 
    print(word)  # Outputs: aa, ab, ba, bb