# /*
#  * ¡Han anunciado un nuevo "The Legend of Zelda"!
#  * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
#  * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
#  * "The Legend of Zelda" de la historia?
#  * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
#  * que tú selecciones.
#  * - Debes buscar cada uno de los títulos y su día de lanzamiento 
#  *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
#  */

from datetime import datetime

# Define the games with their release dates
games = {
    1: {"name": "The Legend of Zelda", "date": datetime(1986, 2, 21)},
    2: {"name": "Zelda II: The Adventure of Link", "date": datetime(1987, 1, 14)},
    3: {"name": "The Legend of Zelda: A Link to the Past", "date": datetime(1991, 11, 21)},
    4: {"name": "The Legend of Zelda: Link's Awakening", "date": datetime(1993, 6, 6)},
    5: {"name": "The Legend of Zelda: Ocarina of Time", "date": datetime(1998, 11, 21)},
    6: {"name": "The Legend of Zelda: Majora's Mask", "date": datetime(2000, 4, 27)},
    7: {"name": "The Legend of Zelda: Oracle of Seasons & Oracle of Ages", "date": datetime(2001, 2, 27)},
    8: {"name": "The Legend of Zelda: The Wind Waker", "date": datetime(2002, 12, 13)},
    9: {"name": "The Legend of Zelda: Four Swords Adventures", "date": datetime(2004, 3, 7)},
    10: {"name": "The Legend of Zelda: The Minish Cap", "date": datetime(2004, 11, 4)},
    11: {"name": "The Legend of Zelda: Twilight Princess", "date": datetime(2006, 11, 19)},
    12: {"name": "The Legend of Zelda: Phantom Hourglass", "date": datetime(2007, 6, 23)},
    13: {"name": "The Legend of Zelda: Spirit Tracks", "date": datetime(2009, 12, 23)},
    14: {"name": "The Legend of Zelda: Skyward Sword", "date": datetime(2011, 11, 18)},
    15: {"name": "The Legend of Zelda: A Link Between Worlds", "date": datetime(2013, 11, 22)},
    16: {"name": "The Legend of Zelda: Tri Force Heroes", "date": datetime(2015, 10, 22)},
    17: {"name": "The Legend of Zelda: Breath of the Wild", "date": datetime(2017, 3, 3)},
    18: {"name": "The Legend of Zelda: Tears of the Kingdom", "date": datetime(2023, 5, 12)}
}

# Show the games to the user
print("List of games:")
for num, game in games.items():
    print(f"{num}: {game['name']}")

# Ask the user to choose two numbers corresponding to the games
selection1 = int(input("\nChoose the first game (write the corresponding number): "))
selection2 = int(input("Choose the second game (write the corresponding number): "))

# Get the dates of the selected games
date_selection1 = games[selection1]["date"]
date_selection2 = games[selection2]["date"]

# Calculate the difference in days between the two releases
days_difference = abs((date_selection1 - date_selection2).days)

# Show the result to the user
print(f"\nBetween {games[selection1]['name']} and {games[selection2]['name']}, there are {days_difference} days.")







