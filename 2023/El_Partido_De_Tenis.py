# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

def win_point():
    return input("Introduzca ganador del punto (P1 o P2): ")

def result(P1, P2):
    points = [0, 15, 30, 40, 'Ventaja']
    return print(f"Resultado del partido: {points[P1]}-{points[P2]}")

def result_advantage(P1, P2):
    points = [0, 15, 30, 40, 'Ventaja']
    if P1 == 3 and P2 == 3:
        return print("Resultado del partido: Deuce")
    elif P1 == 4:
        return print(f"Resultado del partido: {points[P1]} P1")
    else:
        return print(f"Resultado del partido: {points[P2]} P2")

P1, P2 = 0, 0
while P1 < 4 and P2 < 4:
    result(P1, P2)
    point = win_point()
    if point == 'P1':
        P1 += 1
    else:
        P2 += 1

while P1 >= 3 and P1 < 5 and P2 >= 3 and P2 < 5:
    if P1 == 3 and P2 == 3:
        result_advantage(P1, P2)
        point = win_point()
        if point == 'P1':
            P1 += 1
        else:
            P2 += 1
    elif P1 == 4:
        result_advantage(P1, P2)
        point = win_point()
        if point == 'P2':
            P1 -= 1
        else:
            P1 += 1
    else:
        result_advantage(P1, P2)
        point = win_point()
        if point == 'P1':
            P2 -= 1
        else:
            P2 += 1

if P1 == 5 or P1 == 4:
    print('Ha ganado el P1')
elif P2 == 5 or P2 == 4:
    print('Ha ganado el P2')

