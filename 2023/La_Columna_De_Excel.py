# /*
#  * Crea una función que calcule el número de la columna de una hoja de Excel
#  * teniendo en cuenta su nombre.
#  * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#  */

def excel_column_to_number(column):
    result = 0
    for i, letter in enumerate(reversed(column)):
        letter_value = ord(letter) - ord('A') + 1
        result += letter_value * (26 ** i)
    return result

print(excel_column_to_number("A"))
print(excel_column_to_number("Z"))
print(excel_column_to_number("AA"))
print(excel_column_to_number("CA"))







