# /*
#  * La última semana de 2021 comenzamos la actividad de retos de programación,
#  * con la intención de resolver un ejercicio cada semana para mejorar
#  * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
#  *
#  * Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.
#  */

dct = dict(zip("abcdefghijklmnñopqrstuvwxyz", range(1, 28)))

points = 0
while points != 100:
    points = 0
    word = input("Introduzca una palabra sin: ")

    for item in word:
        if item.lower() in dct.keys():
            points += dct[item.lower()]

    if points == 100:
        print("\n¡Lograste 100 puntos!")
    else:
        print("\nPuntuación de la palabra:", points)





