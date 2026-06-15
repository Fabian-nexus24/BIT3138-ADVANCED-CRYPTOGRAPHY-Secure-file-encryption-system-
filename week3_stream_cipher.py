def xor_cipher(text, key):
    result = ""

    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return result

message = "ADVANCED CRYPTOGRAPHY"
key = "SECRET"

encrypted = xor_cipher(message, key)
decrypted = xor_cipher(encrypted, key)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)