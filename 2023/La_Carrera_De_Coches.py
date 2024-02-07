# /*
#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  *
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  */

import random
import time

def race_simulation(track_length):
    car1 = "🚙"
    car2 = "🚗"
    finish_line = "🏁"
    tree = "🌲"
    track1, track2 = generate_tracks(track_length)
    trees_positions = generate_trees(track_length)

    while True:
        # Print tracks
        print_tracks(track1, track2, finish_line, trees_positions, car1, car2, tree)

        time.sleep(1)
        move1 = random.randint(1, 3)
        move2 = random.randint(1, 3)

        # Move cars
        track1, track2 = move_cars(track1, track2, car1, car2, move1, move2, finish_line, trees_positions)

        # Check if any car reached the finish line
        if track1[-1] == finish_line and track2[-1] == finish_line:
            print("It's a tie!")
            break
        elif track1[-1] == finish_line:
            print("Car 1 wins!")
            break
        elif track2[-1] == finish_line:
            print("Car 2 wins!")
            break

def generate_tracks(track_length):
    return "_" * track_length, "_" * track_length

def generate_trees(track_length):
    num_trees = random.randint(1, 3)
    return random.sample(range(1, track_length), num_trees)

def print_tracks(track1, track2, finish_line, trees_positions, car1, car2, tree):
    print("\n", finish_line)
    for i in range(len(track1)):
        if i in trees_positions:
            print(tree, end="")
        else:
            print("_", end="")
    print(car1)

    print("\n", finish_line)
    for i in range(len(track2)):
        if i in trees_positions:
            print(tree, end="")
        else:
            print("_", end="")
    print(car2)

def move_cars(track1, track2, car1, car2, move1, move2, finish_line, trees_positions):
    # Move car 1
    if move1 <= len(track1):
        if track1[-move1] in trees_positions:
            print("💥", end="")
        else:
            track1 = "_" * (len(track1) - move1) + car1
    else:
        track1 = finish_line
    # Move car 2
    if move2 < len(track2):
        if track2[-move2] in trees_positions:
            print("💥", end="")
        else:
            track2 = "_" * (len(track2) - move2) + car2
    else:
        track2 = finish_line
    
    return track1, track2

track_length = int(input("Introduzca un número entero: "))
race_simulation(track_length)







