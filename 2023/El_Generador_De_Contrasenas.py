# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random
import string

def random_lowercase_letter():
    return random.choice(string.ascii_lowercase)

def random_uppercase_letter():
    return random.choice(string.ascii_uppercase)

def random_number():
    return random.choice(string.digits)

def random_symbols():
    return random.choice(string.punctuation)

def generate_password(length, capital, numbers, symbols):
    password = ''
    for _ in range(length):
        options = []
        options.append(random_lowercase_letter())
        if capital:
            options.append(random_uppercase_letter())
        if numbers:
            options.append(random_number())
        if symbols:
            options.append(random_symbols())

        if options:
            password += random.choice(options)
        else:
            password += random_lowercase_letter()
    
    return password

length, capital, numbers, symbols = input("Introduzca la longitud de la contraseña (entre 8 y 16), si quieres letras mayúsculas (S/N), si quieres números (S/N) y si quieres símbolos (S/N). Separados por espacios (| | | |): ").split()
length = int(length)

flag_capital = capital.upper() == 'S'
flag_numbers = numbers.upper() == 'S'
flag_symbols = symbols.upper() == 'S'

print(generate_password(length, flag_capital, flag_numbers, flag_symbols))

