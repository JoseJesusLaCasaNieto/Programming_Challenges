# /*
#  * Crea un programa se encargue de transformar un número binario
#  * a decimal sin utilizar funciones propias del lenguaje que
#  * lo hagan directamente.
#  */

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        binary //= 10
        power += 1
    
    return decimal

binary_number = int(input("Introduzca un número binario: "))

decimal_number = binary_to_decimal(binary_number)
print("Decimal equivalente:", decimal_number)






