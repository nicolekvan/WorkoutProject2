def encrypt_message(original_file, encrypted_file, key):
    try:
        with open(original_file, "r") as source:
            content = source.read()
        
        with open(encrypted_file, "w") as encryption:
            rows = key
            cols = key
            matrix = [['' for _ in range(cols)] for _ in range(rows)]

            index = 0
            for i in range(rows):
                for j in range(cols):
                    if index < len(content):
                        matrix[i][j] = content[index]
                        index += 1
            
            for j in range(cols):
                for i in range(rows):
                    encryption.write((matrix[i][j]))
        
        return encrypted_file
    
    except Exception as e:
        print(e)    

def decrypt_message(encrypted_file, decrypted_file, key):
    try:
        with open(encrypted_file, "r") as source:
            ciphertext = source.read()

        num_rows = len(ciphertext) // key
        remainder = len(ciphertext) % key
        if remainder:
            num_rows += 1

        matrix = [['' for _ in range(key)] for _ in range(num_rows)]
        index = 0
        for j in range(key):
            for i in range(num_rows):
                if i == num_rows - 1 and j >= remainder and remainder != 0:
                    continue
                if index < len(ciphertext):
                    matrix[i][j] = ciphertext[index]
                    index += 1

        plaintext = ''
        for i in range(num_rows):
            for j in range(key):
                if matrix[i][j]:
                    plaintext += matrix[i][j]

        with open(decrypted_file, "w") as decryption:
            decryption.write(plaintext)

        return decrypted_file

    except Exception as e:
        print(f"Error decrypting message: {e}")



