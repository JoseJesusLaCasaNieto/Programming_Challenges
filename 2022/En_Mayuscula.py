# /*
#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

def upper_text(strng):
    strng = strng.split()
    new_str = ''

    for item in strng:
        if new_str:
            new_str += ' '
        new_str += item[0].upper() + item[1:]
    
    return new_str

entrance = input("Introduzca una cadena de texto: ")

print("\nCadena de texto en mayúscula:", upper_text(entrance))






