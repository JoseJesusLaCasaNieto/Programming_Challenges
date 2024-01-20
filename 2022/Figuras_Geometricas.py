# /*
#  * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  * - EXTRA: ¿Eres capaz de dibujar más figuras?
#  */

def draw_square(side):
    for i in range(side):
        for j in range(side):
            print("*", end=" ")
        print()

def draw_triangle(side):
    for i in range(1, side + 1):
        for j in range(i):
            print("*", end=" ")
        print()


print("Seleccione una de las figuras:")
print("1. Cuadrado")
print("2. Triángulo")
    
option = int(input("Introduzca la figura que desee: "))
    
side = int(input("Introduzca el tamaño de la figura: "))
    
if option == 1:
    draw_square(side)
elif option == 2:
    draw_triangle(side)
else:
    print("Selección errónea. Introduzca una de las posibles figuras.")






