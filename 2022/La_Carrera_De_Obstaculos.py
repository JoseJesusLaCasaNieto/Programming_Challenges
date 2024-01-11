# /*
#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  */

def complete_obstacle_course(athlete_actions, track):
    result = ""
    for action, obstacle in zip(athlete_actions, track):
        if action == "run" and obstacle == "_":
            result += "_"
        elif action == "jump" and obstacle == "|":
            result += "|"
        elif action == "jump" and obstacle == "_":
            result += "x"
        elif action == "run" and obstacle == "|":
            result += "/"
        else:
            return False
    print("Course Result:", result)
    return True

athlete_actions = ["run", "jump", "run", "jump", "run"]
track_obstacles = "_|_|_|_|_"

if complete_obstacle_course(athlete_actions, track_obstacles):
    print("\n¡El atleta ha superado la carrera!")
else:
    print("\nEl atleta no ha superado la carrera.")





