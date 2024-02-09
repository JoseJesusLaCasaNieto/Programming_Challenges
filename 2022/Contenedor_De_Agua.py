# /*
#  * Dado un array de números enteros positivos, donde cada uno
#  * representa unidades de bloques apilados, debemos calcular cuantas unidades
#  * de agua quedarán atrapadas entre ellos.
#  *
#  * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
#  *
#  *          ⏹
#  *          ⏹
#  *   ⏹💧💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹⏹⏹
#  *
#  *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
#  *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
#  *   que retiene el agua.
#  */

import numpy as np

array = input("Introduzca números enteros separados por espacios (| | |): ").split()
array = [int(item) for item in array]
max_value = max(array)
matrix = np.zeros((max_value, len(array)), dtype=str)

for i, val in enumerate(array):
    matrix[max_value - val:, i] = '⏹'

for i in range(max_value):
    row = matrix[i]
    idx_block = [idx for idx, val in enumerate(row) if val == '⏹']
    if len(idx_block) > 1:
        for idx in range(idx_block[0]+1, idx_block[-1]):
            if row[idx] == '':
                row[idx] = '💧'

matrix[matrix == ''] = '0'

print("\n", matrix)





