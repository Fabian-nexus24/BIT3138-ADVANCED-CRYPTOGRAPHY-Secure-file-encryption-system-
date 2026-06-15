from cryptography.fernet import Fernet

# Load key
with open("aes_key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read encrypted file
with open("secret.txt.enc", "rb") as file:
    encrypted_data = file.read()

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data)

# Save decrypted file
with open("secret_decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File decrypted successfully!")