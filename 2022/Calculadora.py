# /*
#  * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
#  * resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un
#  *   símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#  *   y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última
#  *   línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han
#  *   podido resolver las operaciones.
#  */

import os

def calculate_result(operations):
    result = 0
    operator = '+'

    for element in operations:
        if element.isdigit() or (element[1:].isdigit() and element[0] == '-'):
            number = float(element)
            if operator == '+':
                result += number
            elif operator == '-':
                result -= number
            elif operator == '*':
                result *= number
            elif operator == '/':
                result /= number
        else:
            operator = element

    return result

rute = os.path.join('2022', 'Challenge21.txt')

try:
    with open(rute, 'r') as f:
        lines = f.read().splitlines()

    result = calculate_result(lines)
    print("The result is:", result)

except Exception as e:
    print("Unable to solve the operations. Error:", str(e))








