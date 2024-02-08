# /*
#  * Crea una función que retorne el número total de bumeranes de
#  * un array de números enteros e imprima cada uno de ellos.
#  * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#  *   seguidos, en el que el primero y el último son iguales, y el segundo
#  *   es diferente. Por ejemplo [2, 1, 2].
#  * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
#  *   y [4, 2, 4]).
#  */

def boomerang(arr):
    result = []
    i = 0
    while i <= len(arr) - 3:       
        if arr[i] == arr[i + 2]:
            result.append((arr[i], arr[i + 1], arr[i + 2]))
        i += 1

    return result

entrance = input("Introduzca una serie de números enteros separados por espacios (| | |): ").split()
entrance = [int(item) for item in entrance]

print("\nTotal de bumeranes en la lista anterior:", boomerang(entrance))


