# /*
#  * Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
#  * indicándole únicamente el tamaño del lado.
#  *
#  * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
#  *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
#  */

def calculate_previous_row(previous_row):
    new_row = [1]
    for i in range(len(previous_row) - 1):
        new_row.append(previous_row[i] + previous_row[i + 1])
    new_row.append(1)
    return new_row

def draw_pascal_triangle(size):
    triangle = [[1]]
    max_width = len(str(2**(size-1))) + 1
    for _ in range(1, size):
        new_row = calculate_previous_row(triangle[-1])
        triangle.append(new_row)

    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width * size))

size = int(input("Introduzca el tamaño del lado del triángulo: "))
draw_pascal_triangle(size)








