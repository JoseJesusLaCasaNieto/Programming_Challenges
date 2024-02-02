# /*
#  * Implementa uno de los algoritmos de ordenación más famosos:
#  * el "Quick Sort", creado por C.A.R. Hoare.
#  * - Entender el funcionamiento de los algoritmos más utilizados de la historia
#  *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
#  *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
#  * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
#  *   donde trabajaremos y entenderemos los más famosos de la historia.
#  */

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

lst = [5, 8, 4, 3, 9, 1]
size = len(lst)
quickSort(lst, 0, size - 1)
print(lst)







