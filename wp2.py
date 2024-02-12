import sys
from pathlib import Path
from encrypt import *
from check_key import *

# python3 wp2.py -e originaltext.txt encryptedtext.txt 11

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error = message

class KeyValidationError(CustomError):
    def __init__(self, message="Key validation error"):
        super().__init__(message)

def get_input():
    if len(sys.argv) != 5:
        print("Error: Please enter correct arguments: python3 wp2.py command file.txt file.txt key")

    elif len(sys.argv) == 5:
        command = sys.argv[1]
        original_text = sys.argv[2]
        encrypted_text = sys.argv[3]
        key = sys.argv[4]

        return command, original_text, encrypted_text, key
    else:
        print("Error: Please enter in the proper format | python3 wp2.py command file.txt file.txt key")
        

def get_path(original_text, encrypted_text):
    try:
        directory = "."

        original_file = Path(directory) / original_text
        encrypted_file = Path(directory) / encrypted_text

        original_file.touch()
        encrypted_file.touch()

        return original_file, encrypted_file
    
    except Exception as e:
        print(f"Unexpected Error Occured: {e}")

def main():
    try:
        command, original_text, encrypted_text, key = get_input()
        original_file, encrypted_file = get_path(original_text, encrypted_text)

        if valid_key(key, original_file) == True:

            if command == "-e":
                read = encrypt_message(original_file, encrypted_file, key)

                with open(read, "r") as file:
                    for line in file:
                        print(line.strip())
                
            elif command == "-d":
                read = decrypt_message(original_file, encrypted_file, key)

                with open(read, "r") as file:
                    for line in file:
                        print(line.strip())
            
            else:
                print("Invalid Command:\nOptions: '-e' '-d'")
        else:
            raise KeyValidationError("Invalid Key, Integer Value Only")

    except KeyValidationError as keyError:
        print(keyError)
    except FileNotFoundError as fileNotFound:
        print(fileNotFound)
    except ValueError:
        print("Please make sure all args are strings beside key, which is an integer")

if __name__ == "__main__":
    main()
