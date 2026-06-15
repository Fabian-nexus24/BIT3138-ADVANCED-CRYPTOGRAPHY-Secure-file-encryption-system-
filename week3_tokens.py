import secrets

token = secrets.token_urlsafe(32)

print("Secure Authentication Token:")
print(token)