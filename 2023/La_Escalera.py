# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  *
#  * Ejemplo: 4
#  *         _
#  *       _|
#  *     _|
#  *   _|
#  * _|
#  *
#  */

def stairs(steps):
    if steps == 0:
        print('__')
    elif steps > 0:
        for step in range(steps + 1):
            spaces = ' ' * ((steps - step) * 2)
            step_draw = '_' if step == 0 else '_|'
            print(f"{spaces}{step_draw}")
        
    else:
        for step in range(abs(steps) + 1):
            spaces = " " * ((step * 2) - 1)
            step_draw = "_" if step == 0 else "|_"
            print(f"{spaces}{step_draw}")

entrance = int(input("Introduzca un número entero: "))

print("\n", stairs(entrance))



