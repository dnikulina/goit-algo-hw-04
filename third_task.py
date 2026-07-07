import sys
from pathlib import Path
from colorama import Fore

directory = sys.argv[1]
path = Path(directory)

if not path.exists():
    print("Path does not exist")
    sys.exit()
if not path.is_dir():
    print("This is not a directory")
    sys.exit()

def show_file_structure(path, level = 1):
    for element in path.iterdir():
        indent = "    " * level
        if element.is_dir():
            print(f"{indent}{Fore.BLUE} {element.name} {Fore.RESET}")
            show_file_structure(element, level+1)   
        if element.is_file():
            print(f"{indent}{Fore.YELLOW} {element.name} {Fore.RESET}")    

show_file_structure(path)