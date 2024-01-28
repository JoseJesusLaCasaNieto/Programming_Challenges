# /*
#  * Dado un array de enteros ordenado y sin repetidos,
#  * crea una función que calcule y retorne todos los que faltan entre
#  * el mayor y el menor.
#  * - Lanza un error si el array de entrada no es correcto.
#  */

def find_missing(array):
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            raise ValueError("El array no está ordenado o contiene valores repetidos.")

    smallest = array[0]
    largest = array[-1]
    range_set = set(range(smallest, largest + 1))
   
    missing = list(range_set - set(array))
    
    return sorted(missing)

entrance = input("Introduzca una lista de números, ordenados y no repetidos, separados por espacios (| |): ").split()
array = [int(item) for item in entrance]
print("\nElementos perdidos:", find_missing(array))








