# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */

entrance = input("Introduzca un listado con los pares de cada jugada, separados por espacios y las rondas por comas (| |,| |): ").split(',')

points_1 = 0
points_2 = 0
for item in entrance:
    P1, P2 = item.split()
    if P1 == '🗿' and (P2 == '✂️' or P2 == '🦎'):
        points_1 += 1
    elif P1 == '🗿' and (P2 == '📄' or P2 == '🖖'):
        points_2 += 1
    elif P1 == '📄' and (P2 == '🗿' or P2 == '🖖'):
        points_1 += 1
    elif P1 == '📄' and (P2 == '✂️' or P2 == '🦎'):
        points_2 += 1
    elif P1 == '✂️' and (P2 == '📄' or P2 == '🦎'):
        points_1 += 1
    elif P1 == '✂️' and (P2 == '🗿' or P2 == '🖖'):
        points_2 += 1
    elif P1 == '🦎' and (P2 == '📄' or P2 == '🖖'):
        points_1 += 1
    elif P1 == '🦎' and (P2 == '🗿' or P2 == '✂️'):
        points_2 += 1
    elif P1 == '🖖' and (P2 == '🗿' or P2 == '✂️'):
        points_1 += 1
    else:
        points_2 += 1

if points_1 > points_2:
    print("\nPlayer 1")
elif points_1 < points_2:
    print("\nPlayer 2")
else:
    print("Tie")