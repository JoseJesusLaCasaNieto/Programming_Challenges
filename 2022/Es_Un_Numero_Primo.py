# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

prime_numbers = []

for number in range(1, 101):
    i = 0
    for item in range(1, number + 1):
        if number % item == 0:
            i += 1
        
    if i == 2:
        prime_numbers.append(number)
        
print(prime_numbers)
