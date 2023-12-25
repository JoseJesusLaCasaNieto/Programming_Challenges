# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

word1, word2 = input("Introduzca dos palabras separadas por espacios: ").split()
word1, word2 = word1.lower(), word2.lower()

def anagrama(word1, word2):
    if word1 == word2:
        return False
    
    for item in word2:
        if item not in word1:
            return False
        else:
            return True
    
print(anagrama(word1, word2))

