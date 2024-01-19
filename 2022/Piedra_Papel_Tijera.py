# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#  *   o "S" (tijera).
#  * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#  */

def calculate_winner(matches):
    player_1 = 0
    player_2 = 0

    for play in matches:
        if play[0] == play[1]:
            continue
        elif (play[0] == "R" and play[1] == "S") or \
             (play[0] == "S" and play[1] == "P") or \
             (play[0] == "P" and play[1] == "R"):
            player_1 += 1
        else:
            player_2 += 1

    if player_1 > player_2:
        return "Player 1"
    elif player_2 > player_1:
        return "Player 2"
    else:
        return "Tie"

example_matches = [("R", "S"), ("S", "R"), ("P", "S")]
result = calculate_winner(example_matches)
print(f"The winner is: {result}")






