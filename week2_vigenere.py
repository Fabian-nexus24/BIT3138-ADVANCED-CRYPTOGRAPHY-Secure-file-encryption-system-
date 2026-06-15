def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += char

    return result


message = input("Enter message: ")
key = input("Enter keyword: ")

encrypted = vigenere_encrypt(message, key)

print("\nEncrypted Message:", encrypted)