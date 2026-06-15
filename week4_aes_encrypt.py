from cryptography.fernet import Fernet

# Generate and save key
key = Fernet.generate_key()

with open("aes_key.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# Read file
with open("secret.txt", "rb") as file:
    data = file.read()

# Encrypt
encrypted_data = cipher.encrypt(data)

# Save encrypted file
with open("secret.txt.enc", "wb") as file:
    file.write(encrypted_data)

print("File encrypted successfully!")