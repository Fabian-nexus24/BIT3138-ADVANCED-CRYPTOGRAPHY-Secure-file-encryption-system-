import hashlib

passwords = ["123456", "password", "admin123", "Secure@2026"]

for pwd in passwords:
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    print(f"{pwd} -> {hashed}")