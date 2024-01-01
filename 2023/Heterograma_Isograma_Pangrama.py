# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */

def heterogram(x):
    letters = set()

    for letter in x:
        if letter.isalpha():
            if letter.lower() in letters:
                return False
            letters.add(letter.lower())

    return True

def isogram(x):
    letters = {}

    for letter in x:
        if letter.isalpha():
            letters[letter.lower()] = letters.get(letter.lower(), 0) + 1

    iterations = set(letters.values())
    
    return len(iterations) == 1

def pangram(x):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    letters = set(letter.lower() for letter in x if letter.isalpha())

    return letters == alphabet

entrance = input("Introduzca una frase: ")

if heterogram(entrance):
    print("\nLa entrada es un heterograma.")
elif isogram(entrance):
    print("\nLa entrada es un isograma.")
elif pangram(entrance):
    print("\nLa entrada es un pangrama.")
else:
    print("\nLa entrada no es un histograma, isograma o pangrama.")




