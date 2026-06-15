from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Create cipher object
cipher = Fernet(key)

# Message to encrypt
message = b"Hello Advanced Cryptography"

# Encrypt
encrypted = cipher.encrypt(message)

print("Original Message:", message)
print("Encrypted Message:", encrypted)