# /*
#  * Crea una función que imprima los 30 próximos años bisiestos
#  * siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.
#  */

def leap_years(starting_year):
    lst = []
    while len(lst) < 30:
        if (starting_year % 4 == 0 and starting_year % 100 != 0) or (starting_year % 400 == 0):
            lst.append(starting_year)
        starting_year += 1
    
    return lst

entrance = int(input("Introduzca un año: "))

print("\n{}".format(leap_years(entrance)))



