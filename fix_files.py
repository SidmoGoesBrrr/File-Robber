from cryptography.fernet import Fernet
import os

# Use the same key that was used for encryption
key = b'a4OexdF2N27LLFHt_eFdKe9zK5a98DZuyD2oeJywGJs='
cipher_suite = Fernet(key)

# Define the directory containing your .meow files
directory_path = 'to_encrypt'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.meow'):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            # Decrypt data
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            # Write the decrypted data back to a file, removing the .meow extension
            original_file_path = file_path.rsplit('.meow', 1)[0]
            with open(original_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
        # Optionally, remove the encrypted file
        os.remove(file_path)

print("Decryption complete.")
