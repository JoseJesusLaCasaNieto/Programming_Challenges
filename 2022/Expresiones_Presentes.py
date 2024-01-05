# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

entrance = input("Introduzca dos expresiones separadas por una coma (|,|): ").split(',')

if len(entrance) > 1 and entrance[1].strip().startswith(' '):
    entrance_1, entrance_2 = entrance[0], entrance[1].strip()
else:
    entrance_1, entrance_2 = entrance[0], entrance[1] if len(entrance) > 1 else None

def string_comparison(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    result_1 = ''
    result_2 = ''
    for item in str_1:
        if item in str_1 and item not in str_2 and item not in result_1:
            result_1 += item
    
    for item in str_2:
        if item in str_2 and item not in str_1 and item not in result_2:
            result_2 += item
    
    return result_1, result_2

output_1, output_2 = string_comparison(entrance_1, entrance_2)

print(f"\nResultados: {output_1} | {output_2}")




