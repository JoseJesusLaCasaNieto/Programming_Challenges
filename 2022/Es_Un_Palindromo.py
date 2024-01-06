# /*
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */

entrance = input("Introduzca una expresión: ")

def spaces(entrance):
    new_entrance = ''
    for item in entrance:
        if item.isalpha():
            new_entrance += item.lower()
        
    return new_entrance

def palindrome(entrance):

    first_half = []
    second_half = []

    if len(entrance) % 2 == 0:
        mes_number = int(len(entrance) / 2)
        for item in entrance[:mes_number]:
            if item.isalpha():
                first_half.append(item)
        
        for item in entrance[-1:mes_number - 1:-1]:
            if item.isalpha():
                second_half.append(item)

        if first_half == second_half:
            return True
        else:
            return False
    else:
        for item in entrance[:int(len(entrance) / 2)]:
            if item.isalpha():
                first_half.append(item)
        
        for item in entrance[-1:int(len(entrance) / 2):-1]:
            if item.isalpha():
                second_half.append(item)

        if first_half == second_half:
            return True
        else:
            return False
    
if palindrome(spaces(entrance)):
    print("\nLa expresión es un palíndromo.")
else:
    print("\nLa expresión no es un palíndromo.")



