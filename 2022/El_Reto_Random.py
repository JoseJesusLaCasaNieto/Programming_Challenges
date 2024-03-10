# /*
#  * Crea tu propio enunciado para que forme parte de los retos de 2023.
#  * - Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir
#  * un estilosemejante a los que hemos realizado durante el año.
#  * - Si quieres también puedes proponer tu propia solución al reto
#  *   (en el lenguaje que quieras).
#  */

import random
import string

def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    while True:
        password = ''.join(random.choices(all_chars, k=random.randint(8, 16)))
        if (any(c in lowercase_letters for c in password) and
            any(c in uppercase_letters for c in password) and
            any(c in digits for c in password) and
            any(c in special_chars for c in password)):
            return password

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    if num_passwords <= 0:
        print("Number of passwords must be a positive integer.")
        return

    print("Generated passwords:")
    for _ in range(num_passwords):
        print(generate_password())

if __name__ == "__main__":
    main()




