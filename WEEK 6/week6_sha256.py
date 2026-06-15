import hashlib

message = input("Enter text to hash: ")

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(hash_value)