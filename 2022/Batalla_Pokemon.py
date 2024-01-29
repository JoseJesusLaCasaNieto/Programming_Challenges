# /*
#  * Crea un programa que calcule el daño de un ataque durante
#  * una batalla Pokémon.
#  * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
#  * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#  * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
#  *   (buscar su efectividad)
#  * - El programa recibe los siguientes parámetros:
#  *  - Tipo del Pokémon atacante.
#  *  - Tipo del Pokémon defensor.
#  *  - Ataque: Entre 1 y 100.
#  *  - Defensa: Entre 1 y 100.
#  */

def calculate_effectiveness(attacker, defender):
    effectiveness = {
        'Water': {'Fire': 2, 'Grass': 0.5, 'Electric': 1},
        'Fire': {'Water': 0.5, 'Grass': 2, 'Electric': 1},
        'Grass': {'Water': 2, 'Fire': 0.5, 'Electric': 1},
        'Electric': {'Water': 2, 'Fire': 1, 'Grass': 0.5}
    }
    return effectiveness[attacker].get(defender, 1)

def calculate_damage(attacker, defender, attack, defense):
    effectiveness = calculate_effectiveness(attacker, defender)
    damage = 50 * (attack / defense) * effectiveness
    return damage

attacker_type = input("Attacker's Pokémon type (Water, Fire, Grass, Electric): ")
defender_type = input("Defender's Pokémon type (Water, Fire, Grass, Electric): ")
attack_stat = int(input("Attacker's attack stat (between 1 and 100): "))
defense_stat = int(input("Defender's defense stat (between 1 and 100): "))

damage = calculate_damage(attacker_type, defender_type, attack_stat, defense_stat)
print("The damage dealt is: {:.1f}".format(damage))







