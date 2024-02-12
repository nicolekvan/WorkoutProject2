def __is_integer(key):
    return isinstance(key, int)

def _is_valid_length(key, file_size):
    return key < file_size

def valid_key(key, file_path):
    
    if not __is_integer(key):
        print("Error: Key must be an integer.")
        return False

    try:
        with open(file_path, 'rb') as f:
            file_size = len(f.read())
            if not _is_valid_length(key, file_size):
                print(f"Error: Key must be smaller than the document size ({file_size}).")
                return False
    except FileNotFoundError:
        print("Error: File not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

    return True
