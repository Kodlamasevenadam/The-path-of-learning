import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

key = chars.copy()

random.shuffle(key)

# encryption
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"plain text: {plain_text}")
print(f"encrypted text: {cipher_text}")

# decryption
plain_text = ""
cipher_text = input("Enter the text to decrypt: ")

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text: {cipher_text}")
print(f"decrypted text: {plain_text}")
