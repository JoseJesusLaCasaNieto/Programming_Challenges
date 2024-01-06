# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

def dec_to_hex_oct(decimal):
    decimal = int(decimal)
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:'8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    oct_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}

    hexadecimal = []
    octal = []
    
    # Conversión a hexadecimal.
    decimal_hex = decimal
    while decimal_hex > 0:
        rest = decimal_hex % 16
        hexadecimal.append(hex_dict[rest])
        decimal_hex //= 16

    hexadecimal = hexadecimal[::-1]

    # Conversión a octal.
    decimal_oct = decimal
    while decimal_oct > 0:
        rest = decimal_oct % 8
        octal.append(oct_dict[rest])
        decimal_oct //= 8
    
    octal = octal[::-1]

    return ''.join(hexadecimal), ''.join(octal)

entrance = input("Introduzca un número decimal: ")

hexadecimal_entrance, octal_entrance = dec_to_hex_oct(entrance)
print("\nHexadecimal:", hexadecimal_entrance)
print("Octal:", octal_entrance)



