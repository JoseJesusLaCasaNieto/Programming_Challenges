# /*
#  * Los primeros dispositivos móviles tenían un teclado llamado T9
#  * con el que se podía escribir texto utilizando únicamente su
#  * teclado numérico (del 0 al 9).
#  *
#  * Crea una función que transforme las pulsaciones del T9 a su
#  * representación con letras.
#  * - Debes buscar cuál era su correspondencia original
#  * - Cada bloque de pulsaciones va separado por un guión.
#  * - Si un bloque tiene más de un número, debe ser siempre el mismo.
#  * - Ejemplo:
#  *     Entrada: 6-666-88-777-33-3-33-888
#  *     Salida: MOUREDEV
#  */

def t9_to_text(sequence: str) -> str:

    if check_t9(sequence):

        t9 = [" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

        text = ""

        for number_sequence in sequence.split("-"):
            
            number = int(number_sequence[0])
            key = t9[number]
            text += key[(len(number_sequence) - 1) % len(key)]

        return text

    return "Error"

def check_t9(sequence: str) -> bool:

    if not sequence:
        return False

    for number_sequence in sequence.split("-"):

        reference = number_sequence[0]

        for item in number_sequence:
            if not item.isdigit() or item != reference:
                return False
    
    return True

print(t9_to_text("6-666-88-777-33-3-33-888"))
print(t9_to_text("6-666-88-777-33-0-3-33-888"))
print(t9_to_text("6-676-88-777-33-3-33-888"))
print(t9_to_text("6-6a6-88-777-33-3-33-888"))
print(t9_to_text(""))
print(t9_to_text("2222"))









