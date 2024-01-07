# /*
#  * Crea una función que sea capaz de transformar Español al lenguaje básico
#  * del universo Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */

def translate_to_aurebesh(text):
    traduction = ''
    for letter in text:
        if letter in esp_aurebesh:
            traduction += esp_aurebesh.get(letter)
        else:
            traduction += letter

    return traduction

def translate_to_spanish(text):
    traduction = ''
    current_word = ''

    for char in text:
        if char == ' ':
            traduction += ' '
            continue
        
        current_word += char

        if current_word in aurebesh_esp:
            traduction += aurebesh_esp[current_word]
            current_word = ''

    return traduction

def detect_language(text):
    for aurebesh_word in aurebesh_esp.keys():
        if aurebesh_word in text:
            return True

esp_aurebesh = {'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'd': 'dorn', 'e': 'esk', 'f': 'forn',
                'g': 'grek', 'h': 'herf', 'i': 'isk', 'j': 'jenth', 'k': 'krill', 'l': 'leth',
                'm': 'mern', 'n': 'nern', 'o': 'osk', 'p': 'peth', 'q': 'qek', 'r': 'resh',
                's': 'senth', 't': 'trill', 'u': 'usk', 'v': 'vev', 'w': 'wesk', 'x': 'xesh',
                'y': 'yirt', 'z': 'zerek'}

aurebesh_esp = {v: k for k, v in esp_aurebesh.items()}

entrance = input("Introduzca un texto a traducir: ")
entrance = entrance.lower()

if detect_language(entrance):
    traduction = translate_to_spanish(entrance)
    print("\nTraducción del texto a español:", traduction)
else:
    traduction = translate_to_aurebesh(entrance)
    print("\nTraducción del texto a aurebesh:", traduction)





