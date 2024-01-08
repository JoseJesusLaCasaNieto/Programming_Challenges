# /*
#  * Escribe una función que calcule si un número dado es un número de Armstrong
#  * (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información
#  * al respecto.
#  */

def str_to_int(text):
    number_lst = []
    for item in text:
        item = int(item)
        number_lst.append(item)
    
    return number_lst

def armstrong(lst):
    result = 0
    for item in lst:
        result += item ** len(lst)
    
    return result

entrance = input("Introduzca un número entero positivo: ")

print("\nResultado número de Armstrong:", armstrong(str_to_int(entrance)))







