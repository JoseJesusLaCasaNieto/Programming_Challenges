# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

lst = [0, 1]

i = 2
while i < 50:
    lst.append(lst[-1] + lst[-2])
    i += 1

print(lst)
print(len(lst))
