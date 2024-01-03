# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

def string_to_morse(strng):
    str_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 
                  'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 
                  'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                  'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.', '0': '-----'}
    
    morse = ''
    for word in strng:
        word = word.lower()
        for letter in word:
            morse += str_morse_dict[letter]
            morse += ' '
        morse += '  '
    
    return morse

def morse_to_string(strng):
    str_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 
                  'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 
                  'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                  'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.', '0': '-----'}
    
    string = []
    for word in strng:
        letters = word.split(' ')
        for letter in letters:
            string += [i for i in str_morse_dict if str_morse_dict[i] == letter]
        string += [' ']

    return string
    
entrance = input("Introduzca un string: ")

if entrance[0] in '-.':
    entrance = entrance.split('  ')
    word_list = morse_to_string(entrance)
    print(''.join(word_list))
else:
    entrance = entrance.split()
    print(string_to_morse(entrance))


