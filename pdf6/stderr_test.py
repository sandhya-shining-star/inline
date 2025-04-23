# Suppress stderr output 
import sys 
import contextlib 
import os 
@contextlib.contextmanager 
def no_stderr(): 
    with open(os.devnull, "w") as devnull: 
        old_stderr = sys.stderr 
        sys.stderr = devnull 
        try: 
            yield 
        finally: 
            sys.stderr = old_stderr 
with no_stderr(): 
    print("This goes to stdout", file=sys.stderr)  # Suppressed 
print("This is visible") 
