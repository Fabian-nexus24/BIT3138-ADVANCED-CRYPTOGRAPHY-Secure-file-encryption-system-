import hashlib

password = input("Create Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nStored Password Hash:")
print(hashed_password)