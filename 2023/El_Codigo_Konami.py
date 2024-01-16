# /*
#  * Crea un programa que detecte cuando el famoso "Código Konami" se ha
#  * introducido correctamente desde el teclado.
#  * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
#  */

konami_code = ('Arriba', 'Arriba', 'Abajo', 'Abajo', 'Izquierda', 'Derecha', 'Izquierda', 'Derecha', 'B', 'A')

entrance = input("Introduzca el Código Konami separado por espacios (| | |): ").split()

print(konami_code)
print(entrance)

if entrance == list(konami_code):
    print("\nEs correcto!")
else:
    print("\nCódigo incorrecto.")







