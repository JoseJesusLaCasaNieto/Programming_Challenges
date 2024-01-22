# /*
#  * Crea una función que sea capaz de leer el número representado por el ábaco.
#  * - El ábaco se representa por un array con 7 elementos.
#  * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#  *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
#  * - El primer elemento del array representa los millones, y el último las unidades.
#  * - El número en cada elemento se representa por las cuentas que están a
#  *   la izquierda del alambre.
#  *
#  * Ejemplo de array y resultado:
#  * ["O---OOOOOOOO",
#  *  "OOO---OOOOOO",
#  *  "---OOOOOOOOO",
#  *  "OO---OOOOOOO",
#  *  "OOOOOOO---OO",
#  *  "OOOOOOOOO---",
#  *  "---OOOOOOOOO"]
#  *
#  *  Resultado: 1.302.790
#  */

def abacus(ent):
    result = ''
    for row in ent:
        for position, item in enumerate(row):
            if item != 'O':
                result += str(position)
                break

    return int(result)

abacus_example = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

result = abacus(abacus_example)
print("Result:", result)








