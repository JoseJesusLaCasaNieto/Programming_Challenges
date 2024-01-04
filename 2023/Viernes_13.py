# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import calendar

def friday_13(year, month):
    return calendar.weekday(year, month, 13) == 4

year, month = input("Introduzca un año y un mes, separados por espacios (| |): ").split()
year = int(year)
month = int(month)

if friday_13(year, month):
    print("\nExiste un viernes 13 en el mes y año indicados.")
else:
    print("\nNo existe un viernes 13 en el mes y año indicados.")





