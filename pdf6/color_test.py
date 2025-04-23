# Use colorama for colored output 
from colorama import init, Fore 
init() 
print(f"{Fore.GREEN}Success!{Fore.RESET}") 
print(f"{Fore.RED}Error occurred{Fore.RESET}")