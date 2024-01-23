# /*
#  * Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#  *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#  *   o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#  *   automáticamente.
#  */

def bubblesort(lst, typ):   # Algoritmo de ordenación de burbuja.
    if typ == 'Asc':
        for num in range(len(lst)-1, 0, -1):
            for i in range(num):
                if lst[i] > lst[i+1]:
                    temp = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = temp
    
        return lst
    
    if typ == 'Desc':
        for num in range(len(lst)):
            for i in range(len(lst)-1, num, -1):
                if lst[i] > lst[i-1]:
                    temp = lst[i]
                    lst[i] = lst[i-1]
                    lst[i-1] = temp
    
        return lst

typ = input("Introduzca un parámetro (Asc o Desc): ")
lst = [5, 8, 4, 3, 9, 1]
print(bubblesort(lst, typ))





