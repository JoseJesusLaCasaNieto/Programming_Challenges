# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */

entrance = input("Introduzca una URL: ")

number = ''
number_lst = []
i = -1
for item in entrance:
    i += 1
    if item in '0123456789':
        number += item
        if i + 1 == len(entrance) or entrance[i+1] not in '0123456789':
            number_lst.append(number)
            number = ''

print(number_lst)


