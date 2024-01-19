# /*
#  * Crea una función que reciba una expresión matemática (String)
#  * y compruebe si es correcta. Retornará true o false.
#  * - Para que una expresión matemática sea correcta debe poseer
#  *   un número, una operación y otro número separados por espacios.
#  *   Tantos números y operaciones como queramos.
#  * - Números positivos, negativos, enteros o decimales.
#  * - Operaciones soportadas: + - * / %
#  *
#  * Ejemplos:
#  * "5 + 6 / 7 - 4" -> true
#  * "5 a 6" -> false
#  */

def validate_expression(expression):
    operators = set(["+", "-", "*", "/", "%"])
    elements = expression.split()

    if len(elements) % 2 == 0:
        return False 

    for i, elem in enumerate(elements):
        if i % 2 == 0:
            try:
                float(elem)
            except ValueError:
                return False
        else:
            if elem not in operators:
                return False

    return True

expression1 = "5 + 6 / 7 - 4"
expression2 = "5 a 6"

result1 = validate_expression(expression1)
result2 = validate_expression(expression2)

print(f"The expression '{expression1}' is valid: {result1}")
print(f"The expression '{expression2}' is valid: {result2}")





