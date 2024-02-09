import sys
from pathlib import Path

def get_input():
    while True:
        if len(sys.argv) != 6:
            print("Error: Please enter in the proper format | python3 wp2.py command file.txt file.txt key")
            continue
        elif len(sys.argv) == 6:
            command = sys.argv[1]
            original_text = sys.argv[2]
            encrypted_text = sys.argv[3]
            key = sys.arv[4]

            return command, original_text, encrypted_text, key
        else:
            print("Error: Please enter in the proper format | python3 wp2.py command file.txt file.txt key")
            continue

def get_path(original_text, encrypted_text):
    directory = "."

    original_file = Path(directory) / original_text
    encrypted_file = Path(directory) / encrypted_text

    return original_file, encrypted_file

def encrypt_message(original_file, key):
    pass

def decrypt_message(encrypted_file, key):
    pass

def write_to_encrypted_file(original_text, encrypted_text):
    try:
        with open(original_text, "r") as source:
            content = source.readlines()

        with open(encrypted_text, "w") as encryption:
            encryption.write(FIXME)

        return encrypted_text
    except FileNotFoundError as e:
        print(f"{e}")

def main():
    try:
        command, original_text, encrypted_text, key = get_input()
        original_file, encrypted_file = get_path(original_text, encrypted_text)

        if command == "-e":
            encrypt_message(original_file, key)
            pass
        elif command == "-d":
            decrypt_message(encrypted_file, key)
            pass

        encryption = write_to_encrypted_file(original_text, encrypted_text)

        with open(encryption, "r") as file:
            for line in file:
                print(line.strip())
    except:
        FIXME:
        pass

if __name__ == "__main__":
    main()
