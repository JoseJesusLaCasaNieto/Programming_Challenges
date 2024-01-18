# /*
#  * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
#  * ¿De cuántas maneras eres capaz de hacerlo?
#  * Crea el código para cada una de ellas.
#  */

import numpy as np

for item in range(1, 101):
    print(item)

for item in np.arange(1, 101):
    print(item)

i = 1
while i < 101:
    print(i)
    i += 1

list(map(lambda x: print(x), range(1, 101)))

[print(item) for item in range(1, 101)]

counter = iter(range(1, 101))
while True:
    try:
        print(next(counter))
    except StopIteration:
        break


