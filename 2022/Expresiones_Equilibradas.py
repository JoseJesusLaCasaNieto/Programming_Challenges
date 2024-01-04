# /*
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  */

def balanced(entrance):
    item_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for item in entrance:
        if item in '{[(':
            stack.append(item)
        elif item in '}])':
            if item_dict[item] == stack[-1]:
                stack.pop()
            else:
                return False

    return True

entrance = input("Introduzca una expresión a analizar: ")

if balanced(entrance):
    print("\nLa expresión está equilibrada.")
else:
    print("\nLa expresión no está equilibrada.")




