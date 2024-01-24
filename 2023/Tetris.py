# /*
#  * Crea un programa capaz de gestionar una pieza de Tetris.
#  * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
#  * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#  *   🔳
#  *   🔳🔳🔳
#  * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#  *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#  *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en
#  *   la pantalla de juego.
#  * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
#  * - Debes tener en cuenta los límites de la pantalla de juego.
#  */

import numpy as np
from enum import Enum
import keyboard
import time

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def print_screen(screen):
    print("\nPantalla Tetris\n")
    for row in screen:
        for item in row:
            if item == 0:
                print('🔲', end='')
            else:
                print('🔳', end='')
        print()

def move_piece(screen, movement: Movement, rotation):

    new_screen = np.zeros(shape=(10, 10))

    rotation_item = 0
    rotations = [[(1, 1), (0, 0), (-2, 0), (-1, -1)],
                 [(0, 1), (-1, 0), (0, -1), (1, -2)],
                 [(0, 2), (1, 1), (-1, 1), (-2, 0)],
                 [(0, 1), (1, 0), (2, -1), (1, -2)]]
    new_rotation = rotation

    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    for row_index, row in enumerate(screen):
        for col_index, item in enumerate(row):
            if item == 1:
                new_row_index = 0
                new_col_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_col_index = col_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_col_index = col_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_col_index = col_index - 1
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_col_index = col_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1
                
                if new_row_index > len(row) - 1 or new_col_index > len(row) - 1 or new_col_index < 0:
                    print("\nNo se puede realizar el movimiento")
                    return screen, rotation
                else:
                    new_screen[new_row_index][new_col_index] = 1
    
    print_screen(new_screen)

    return new_screen, new_rotation

def add_piece(screen):
    screen[0][0] = 1
    screen[1][:3] = 1
    return screen, 0

def tetris():
    screen = np.zeros(shape=(10, 10))
    screen, rotation = add_piece(screen)
    print_screen(screen)

    while(True):
        time.sleep(0.1)

        if keyboard.is_pressed('esc'):
            break
        elif keyboard.is_pressed('down'):
            screen, rotation = move_piece(screen, Movement.DOWN, rotation)
        elif keyboard.is_pressed('right'):
            screen, rotation = move_piece(screen, Movement.RIGHT, rotation)
        elif keyboard.is_pressed('left'):
            screen, rotation = move_piece(screen, Movement.LEFT, rotation)
        elif keyboard.is_pressed('space'):
            screen, rotation = move_piece(screen, Movement.ROTATE, rotation)

tetris()








