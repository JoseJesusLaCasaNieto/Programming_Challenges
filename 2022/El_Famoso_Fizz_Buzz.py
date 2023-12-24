# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print('fizzbuzz')
    elif item % 3 == 0:
        print('fizz')
    elif item % 5 == 0:
        print('buzz')
    else:
        print(item)
