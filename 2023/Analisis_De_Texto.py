# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.
#  */

def text_analysis(strng):
    words = strng.split()
    total_words = len(words)
    
    if total_words == 0:
        return 'No hay palabras en el texto.'

    mean_long = sum(len(word) for word in words) / len(words)

    sentences_num = strng.count('.')
    
    words_not_dot = []
    for word in words:
        if word[-1] == '.':
            word = word[:-1]
            words_not_dot.append(word)
        else:
            words_not_dot.append(word)
    
    max_word = max(words_not_dot, key=len)

    result = f"Número total de palabras: {total_words}\n" \
             f"Longitud media de las palabras: {mean_long:.2f}\n" \
             f"Número de oraciones del texto: {sentences_num}\n" \
             f"Encuentre la palabra más larga: {max_word}"
    
    return result

entrance = input("Introduzca una cadena de caracteres: ")

print(f"\n{text_analysis(entrance)}")










