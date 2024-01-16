# /*
#  * Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes
#  *   de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes
#  *   de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

def equals(array1, array2, boolean):
    result = []
    if boolean:
        for item in array1:
            if item in array2:
                result.append(item)
    
    else:
        for item in array1:
            if item not in array2:
                result.append(item)
    
    return result

array1 = [2, 5, 7, 9, 11, 12]
array2 = [1, 3, 6, 8, 10, 12]

print("Array 1:", array1)
print("Array 2:", array2)
print("\nResultado para Bool = True:", equals(array1, array2, True))
print("Resultado para Bool = False:", equals(array1, array2, False))



