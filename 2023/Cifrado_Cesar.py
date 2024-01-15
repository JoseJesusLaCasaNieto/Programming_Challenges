# /*
#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.
#  */

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            uppercase = char.isupper()
            index = ord(char) - ord('A' if uppercase else 'a')
            new_index = (index + shift) % 26
            result += chr(ord('A' if uppercase else 'a') + new_index)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)


text = input("Introduzca el texto: ")
shift = int(input("Introduzca un número de desplazamiento: "))

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\nTexto encriptado:", encrypted_text)
print("Texto desencriptado:", decrypted_text)








