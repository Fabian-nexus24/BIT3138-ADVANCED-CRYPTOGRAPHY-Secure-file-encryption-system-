import hashlib

stored_password = "admin123"

stored_hash = hashlib.sha256(stored_password.encode()).hexdigest()

login_password = input("Enter Password: ")

login_hash = hashlib.sha256(login_password.encode()).hexdigest()

if login_hash == stored_hash:
    print("Login Successful")
else:
    print("Access Denied")