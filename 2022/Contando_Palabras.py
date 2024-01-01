# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

import string

entrance = input("Introduzca el texto a analizar: ").split()

words = {}
for item in entrance:
    if item not in string.punctuation:
        if item.lower() not in words:
            item = item.lower()
            words[item] = 0
            words[item] += 1
        else:
            item = item.lower()
            words[item] += 1

print("\n", words)


