# /*
#  * ¡La Tierra Media está en guerra! En ella lucharán razas leales
#  * a Sauron contra otras bondadosas que no quieren que el mal reine
#  * sobre sus tierras.
#  * Cada raza tiene asociado un "valor" entre 1 y 5:
#  * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
#  *   Númenóreanos (4), Elfos (5)
#  * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
#  *   Huargos (3), Trolls (5)
#  * Crea un programa que calcule el resultado de la batalla entre
#  * los 2 tipos de ejércitos:
#  * - El resultado puede ser que gane el bien, el mal, o exista un empate.
#  *   Dependiendo de la suma del valor del ejército y el número de integrantes.
#  * - Cada ejército puede estar compuesto por un número de integrantes variable
#  *   de cada raza.
#  * - Tienes total libertad para modelar los datos del ejercicio.
#  * Ej: 1 Peloso pierde contra 1 Orco
#  *     2 Pelosos empatan contra 1 Orco
#  *     3 Pelosos ganan a 1 Orco
#  */

import random

good_races = {"Hobbits": 1, "Men of the South": 2, "Dwarves": 3, "Men of Numenor": 4, "Elves": 5}
evil_races = {"Men of the South": 2, "Orcs": 2, "Goblins": 2, "Wargs": 3, "Trolls": 5}

good_army = {race: random.randint(100, 500) for race in good_races}
evil_army = {race: random.randint(100, 500) for race in evil_races}

good_strength = sum(value * count for race, value in good_races.items() for race2, count in good_army.items() if race == race2)
evil_strength = sum(value * count for race, value in evil_races.items() for race2, count in evil_army.items() if race == race2)

if good_strength > evil_strength:
    outcome = "Good triumphs over evil!"
elif good_strength < evil_strength:
    outcome = "Evil conquers all!"
else:
    outcome = "It's a draw! The battle rages on."

print("Good army:", good_army)
print("Evil army:", evil_army)
print("Outcome:", outcome)









