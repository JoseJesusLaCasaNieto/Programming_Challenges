# /*
#  * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
#  * en dos dimensiones.
#  * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
#  *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
#  * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
#  * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que
#  *   tardaron en lograrlo.
#  * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
#  */

def collision(position_a, speed_a, position_b, speed_b):

    xa, ya = position_a
    xb, yb = position_b
    sxa, sya = speed_a
    sxb, syb = speed_b

    if sxa - sxb == 0:
        if xa == xb:
            tx = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        tx = (xb - xa) / (sxa - sxb)

    if sya - syb == 0:
        if ya == yb:
            ty = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        ty = (yb - ya) / (sya - syb)

    if tx == ty:
        t = tx
        x = xa + sxa * tx
        y = ya + sya * ty
        return f"Los objetos colisionan en el punto ({x:.2f}, {y:.2f}) en un tiempo {t:.2f}."
    else:
        return "Los objetos no se encontrarán."

print(collision((0, 0), (1, 1), (1, 2), (0, 1)))

print(collision((2, 0), (0, 1), (0, 2), (1, 0)))

print(collision((0, 0), (10, 5), (100, 50), (-5, -2.5)))





