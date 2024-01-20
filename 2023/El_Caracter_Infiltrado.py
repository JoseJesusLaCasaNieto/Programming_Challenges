# /*
#  * Crea una función que reciba dos cadenas de texto casi iguales,
#  * a excepción de uno o varios caracteres.
#  * La función debe encontrarlos y retornarlos en formato lista/array.
#  * - Ambas cadenas de texto deben ser iguales en longitud.
#  * - Las cadenas de texto son iguales elemento a elemento.
#  * - No se pueden utilizar operaciones propias del lenguaje
#  *   que lo resuelvan directamente.
#  *
#  * Ejemplos:
#  * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
#  * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
#  */

def find_differences(string1, string2):
    if len(string1) != len(string2):
        raise ValueError("Both strings must have the same length.")

    differences = []
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            differences.append(char1)

    return differences

print("Me llamo mouredev\n" + "Me llemo mouredov")
example1 = find_differences("Me llamo mouredev", "Me llemo mouredov")
print(example1)

print("\nMe llamo.Brais Moure\n" + "Me llamo brais moure")
example2 = find_differences("Me llamo.Brais Moure", "Me llamo brais moure")
print(example2)







