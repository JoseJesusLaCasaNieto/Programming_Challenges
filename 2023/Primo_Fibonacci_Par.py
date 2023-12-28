# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  *

def prime_number(number):
    i = 0
    for item in range(1, number + 1):
        if number % item == 0:
            i += 1
    
    if i == 2:
        return 'es primo'
    else:
        return 'no es primo'

def fibonacci(number):
    lst_fibonacci = [0, 1]
    fibonacci_number = lst_fibonacci[-1] + lst_fibonacci[-2]
    while fibonacci_number <= number:
        lst_fibonacci.append(fibonacci_number)
        fibonacci_number = lst_fibonacci[-1] + lst_fibonacci[-2]
    
    if number in lst_fibonacci:
        return 'fibonacci'
    else:
        return 'no es fibonacci'

def even_odd_number(number):
    if number % 2 == 0:
        return 'es par'
    else:
        return 'es impar'

number = input("Introduzca un número entero: ")
number = int(number)

print(f"\nEl número {number} {prime_number(number)}, {fibonacci(number)} y {even_odd_number(number)}")


