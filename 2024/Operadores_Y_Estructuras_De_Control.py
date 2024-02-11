# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

# Arithmetic Operators
result_sum = 10 + 5
result_subtraction = 10 - 5
result_multiplication = 10 * 5
result_division = 10 / 5
result_modulo = 10 % 3
result_exponentiation = 10 ** 2

# Comparison Operators
equality = 10 == 5
inequality = 10 != 5
greater_than = 10 > 5
less_than = 10 < 5
greater_than_or_equal_to = 10 >= 5
less_than_or_equal_to = 10 <= 5

# Logical Operators
logical_and = (10 > 5) and (5 < 3)
logical_or = (10 > 5) or (5 < 3)
logical_not = not (10 > 5)

# Assignment Operators
x = 10
x += 5
x -= 3
x *= 2
x /= 4
x %= 2
x **= 3

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
identity_is = list1 is list2
identity_is_not = list1 is not list2

# Membership Operators
membership_in = 1 in list1
membership_not_in = 4 not in list1

# Bitwise Operators
bitwise_and = 10 & 5
bitwise_or = 10 | 5
bitwise_xor = 10 ^ 5
bitwise_left_shift = 10 << 2
bitwise_right_shift = 10 >> 2

# Conditional Statements
if 10 > 5:
    print("Conditional Statement: If condition is True")

# Iterative Statements
for i in range(5):
    print("Iterative Statement:", i)

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Exception Handling: Division by zero")

# Additional Challenge: Print numbers between 10 and 55, excluding 16 and multiples of 3
print("Numbers between 10 and 55, excluding 16 and multiples of 3:")
for num in range(10, 56):
    if num != 16 and num % 3 != 0:
        print(num, end=' ')







