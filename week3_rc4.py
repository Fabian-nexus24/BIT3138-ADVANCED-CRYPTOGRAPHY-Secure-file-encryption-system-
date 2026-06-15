def rc4(key, plaintext):

    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo Random Generation Algorithm
    i = j = 0
    output = []

    for char in plaintext:

        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]

        output.append(chr(ord(char) ^ K))

    return ''.join(output)


message = "ADVANCED CRYPTOGRAPHY"
key = "SECRET"

encrypted = rc4(key, message)
decrypted = rc4(key, encrypted)

print("Original Message :", message)
print("Encrypted Data   :", encrypted)
print("Decrypted Message:", decrypted)