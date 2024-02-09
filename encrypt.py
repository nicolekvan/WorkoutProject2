def encrypt_message(original_file, encrypted_file, key):
    try:
        with open(original_file, "r") as source:
            content = source.read()
        
        with open(encrypted_file, "w") as encryption:
            rows = key
            cols = key
            matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

            index = 0
            for i in range(rows):
                for j in range(cols):
                    if index < len(content):
                        matrix[i][j] = content[index]
                        index += 1
            
            for j in range(cols):
                for i in range(rows):
                    encryption.write((matrix[i][j]).strip())
        
        return encrypted_file
    
    except Exception as e:
        print(e)    

def decrypt_message(original_file, encrypted_file, key):
    pass
