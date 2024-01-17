# /*
#  * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
#  * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

def euclides_MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return (a * b) // euclides_MCD(a, b)

entrance = input("Introduzca dos números, separados por un espacio (| |): ").split()

if int(entrance[0]) > int(entrance[1]):
    number1 = int(entrance[0])
    number2 = int(entrance[1])
else:
    number1 = int(entrance[1])
    number2 = int(entrance[0])

print(f"\nEl MCD de {number1} y {number2} es {euclides_MCD(number1, number2):.0f}")
print(f"El MCM de {number1} y {number2} es {mcm(number1, number2):.0f}")



