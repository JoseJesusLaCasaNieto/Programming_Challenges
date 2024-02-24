# /*
#  * Crea una función que sea capaz de encriptar y desencriptar texto
#  * utilizando el algoritmo de encriptación de Karaca
#  * (debes buscar información sobre él).
#  */

import random

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Introduzca un texto para encriptar: ")
shift = random.randint(1, 25)
encrypted_text = encrypt(text, shift)
print("\nTexto encriptado:", encrypted_text)
desencrypted_text = decrypt(encrypted_text, shift)
print("\nTexto desencriptado:", desencrypted_text)








