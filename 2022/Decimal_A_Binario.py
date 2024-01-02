# /*
#  * Crea un programa que se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def divisions(n):
    quotient = n // 2
    modulus = n % 2
    return quotient, modulus

quotient = input("Introduzca un número entero: ")
quotient = int(quotient)

binary_number = []

if quotient == 0:
    print("\nNúmero binario: 0")
else:
    while quotient != 0:
        quotient, modulus = divisions(quotient)
        binary_number.append(modulus)

result = "".join(map(str, binary_number[::-1]))
print("\nNúmero binario: {}".format(result))

