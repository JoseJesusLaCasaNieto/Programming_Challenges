# /*
#  * Crea un programa que sea capaz de generar e imprimir todas las
#  * permutaciones disponibles formadas por las letras de una palabra.
#  * - Las palabras generadas no tienen por qué existir.
#  * - Deben usarse todas las letras en cada permutación.
#  * - Ejemplo: sol, slo, ols, osl, los, lso
#  */

from itertools import permutations

def generate_permutations(word):
    perm = permutations(word)

    for p in perm:
        print(''.join(p))

entrance = input("introduzca una palabra: ")
print(f"Todas las permutaciones de '{entrance}':")
generate_permutations(entrance)






