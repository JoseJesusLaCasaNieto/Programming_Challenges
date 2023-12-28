# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def polygon_area(polygon, n, m):
    if polygon == 'triangulo':
        area = n * m / 2
        return area
    else:
        area = n * m
        return area

polygon, n, m = input("Introduzca el nombre del polígono en minúsculas y sin tildes (triangulo, cuadrado o rectangulo) junto con dos parámetros numéricos (base y altura o lado horizontal y lado vertical), separados por espacios (| | |): ").split()
polygon = polygon.lower()
n = float(n)
m = float(m)
    
print("\n Área del polígono: {:.2f}".format(polygon_area(polygon, n, m)))

