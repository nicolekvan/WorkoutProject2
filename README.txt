# WorkoutProject2

Simple file encryption/decryption system that takes sys command line input from user in format 
python wp2.py command originaltext.txt encryptedtext.txt key
Where command is either "-e" for encrypt or "-d" for decryption. The key value should be an integer.
WP2 has 2 classes, the CustomError inherits from the Exception class, from which the custom error KeyValidationError
inherits from.

This program has the main wp2.py file, along with two modules from which wp2 imports all its methods.
Check_key.py is responsible for checking if the key is valid (an integer and key is smaller than file size)
Encrypt.py handles the commands -e and -d, using a 2D matrix to warp/transpose the original message into
a column * key text, then transposes that message into a row * key text. Finally, each row is concatenated
and written to it's assignned profile.
