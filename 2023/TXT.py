# /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
#  * Únicamente el código.
#  *
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero. 
#  */

import os

def manage_file():
    file_name = os.path.join(os.path.dirname(__file__), "text.txt")

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("Current content of the file:\n", content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist. Creating file...")

    with open(file_name, 'a') as file:
        new_text = input("Introduzca el texto y presiona 'Enter' para añadir al archivo (o 'q' para salir): ")

        while new_text.lower() != 'q':
            file.write(new_text + '\n')
            new_text = input("Introduzca más texto (o 'q' para salir): ")

    print("Operación completada.")

manage_file()





