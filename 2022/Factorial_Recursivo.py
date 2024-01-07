# /*
#  * Escribe una función que calcule y retorne el factorial de un número dado
#  * de forma recursiva.
#  */

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
entrance = input("Introduzca un número entero: ")
entrance = int(entrance)

result = factorial(entrance)
print("\nFactorial del número:", result)




