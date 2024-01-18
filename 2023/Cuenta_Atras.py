# /*
#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.
#  */

import time

def countdown(start, secs):
    while start >= 0:
        print(start)
        time.sleep(secs)
        start -= 1
    
entrance = input("Introduzca el número en el que comienza la cuenta y los segundos, separados por espacios (| |): ").split()
entrance = [int(item) for item in entrance]

countdown(entrance[0], entrance[1])




