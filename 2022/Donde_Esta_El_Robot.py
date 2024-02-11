# /*
#  * Calcula dónde estará un robot (sus coordenadas finales) que se
#  * encuentra en una cuadrícula representada por los ejes "x" e "y".
#  * - El robot comienza en la coordenada (0, 0).
#  * - Para idicarle que se mueva, le enviamos un array formado por enteros
#  *   (positivos o negativos) que indican la secuencia de pasos a dar.
#  * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
#  *   luego 5, se detiene, y finalmente 2.
#  *   El resultado en este caso sería (x: -5, y: 12)
#  * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
#  *   que está mirando.
#  * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
#  *   hacia la parte positiva del eje "y".
#  * - El robot tiene un fallo en su programación: cada vez que finaliza una
#  *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
#  *   del reloj.
#  */

def move_robot(steps):
    # Initialize robot's coordinates
    x, y = 0, 0
    # Initialize the direction the robot is facing (y-axis positive at the beginning)
    direction = 0

    # Iterate over the provided steps
    for step in steps:
        # Move the robot in the corresponding direction
        if direction == 0:
            y += step
        elif direction == 1:
            x -= step
        elif direction == 2:
            y -= step
        elif direction == 3:
            x += step

        # Turn 90 degrees counterclockwise
        direction = direction % 4 + 1

    # Return the final coordinates of the robot
    return {'x': x, 'y': y}

# Example of usage
step_sequence = [10, 5, -2]
final_coordinates = move_robot(step_sequence)
print(f"Final coordinates: {final_coordinates}")







