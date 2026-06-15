import secrets

# Generate a secure 32-byte key
key = secrets.token_hex(32)

print("Generated Secure Key:")
print(key)
print("\nKey Length:", len(key))