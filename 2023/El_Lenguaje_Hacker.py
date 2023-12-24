# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
hacker_alphabet = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '1', '^^', '^', '0', '|*', '(_,)', 'I2', '5', '7', '(_)', '\/', '\/\/', '><', 'j', '2']

entrance = input('Introduzca el texto que desee con letras del alfabeto (ABCDEFGHIJKLMNOPQRSTUVWXYZ): ').upper()

hacker_word = ''
for item in entrance:
    i = alphabet.index(item)
    hacker_word += hacker_alphabet[i]

print('\n' + hacker_word)
