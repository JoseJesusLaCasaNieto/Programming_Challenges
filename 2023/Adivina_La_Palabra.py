# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

import numpy as np

def delete_letters(word):
    del_number = round(len(word) * 0.6, 0)
    word = list(word)

    while del_number > 0:
        random_number = np.random.randint(0, len(word))
        word[random_number] = '_'
        del_number -= 1

    return ''.join(word)

def random_word(lst):
    random_number = np.random.randint(0, len(lst))

    return lst[random_number]

def screen(objective, tries):
    print()
    print(objective)
    print("Número de intentos restantes: ", tries)
    tries -= 1
    return input("Introduzca una letra o una palabra: "), tries

def deep_letters(str_1, str_2):
    deep_letters = []

    for position, (original_item, deep_item) in enumerate(zip(str_1, str_2)):
        if deep_item == '_':
            deep_letters.append((original_item, position))
    
    return deep_letters

def apply_letter(word, position, letter):
    lst = list(word)
    lst[position] = letter
    return ''.join(lst)

words = ['bienestar', 'relato', 'paraguas', 'naranja', 'catapultar']
tries = 5

objective_word = random_word(words)
objective_w__d = delete_letters(objective_word)
deep_letters_position = deep_letters(objective_word, objective_w__d)

while tries > 0:
    entrance, tries = screen(objective_w__d, tries)
    entrance = entrance.lower()

    if len(entrance) == 1:
        for tple in deep_letters_position:
            if entrance == tple[0]:
                objective_w__d = apply_letter(objective_w__d, tple[1], entrance)
                if objective_w__d == objective_word:
                    print("\nAcertaste! La palabra es: ", objective_word)
                    tries = 0
    elif len(entrance) == len(objective_word):
        if entrance == objective_word:
            print("\nAcertaste! La palabra es:", objective_word)
            tries = 0






