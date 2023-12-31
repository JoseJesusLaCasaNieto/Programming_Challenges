# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del
#  *   lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */

import time

class GeneratorLCG:
    def __init__(self, seed=int(time.time() * 1000), a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m
    
    def generate_number(self, rnge=(1, 100)):
        self.state = (self.a * self.state + self.c) % self.m
        return rnge[0] + (self.state % (rnge[1] - rnge[0] + 1))

generator = GeneratorLCG()

for _ in range(5):
    random_number = generator.generate_number()
    print("Pseudorandom number between 1 and 100: ", random_number)


