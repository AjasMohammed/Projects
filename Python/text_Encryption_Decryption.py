import random
import string

characters = list(string.punctuation + string.digits + string.ascii_letters + ' ')
key = characters.copy()
random.shuffle(key)


def encrypt(text):
    cipher_text = ""
    for char in text:
        index = characters.index(char)
        cipher_text += key[index]
    return cipher_text


def decrypt(text):
    plain_text = ""
    for char in text:
        index = key.index(char)
        plain_text += characters[index]
    return plain_text


user = input("Enter your Text: \n>>> ")

encryption = encrypt(user)
print(f"Encrypted Text : {encryption}")

decryption = decrypt(encryption)
print(f"Decrypted Text : {decryption}")
