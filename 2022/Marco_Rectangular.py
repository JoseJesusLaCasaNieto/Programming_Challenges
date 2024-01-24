# /*
#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********
#  */

def text_frame(txt):
    frame = ''
    max_len = 0
    for item in txt:
        if len(item) > max_len:
            max_len = len(item) + 2
    
    frame += '*' * (max_len + 4) + '\n'
    for item in txt:
        frame += '*' + ' ' + item + ' ' * (max_len - len(item) + 1) + '*' + '\n'
    
    frame += '*' * (max_len + 4) + '\n'
    return frame

entrance = input('Introduzca un texto: ').split()

print('\n{}'.format(text_frame(entrance)))





