# /*
#  * Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  * y retorne su resultado en milisegundos.
#  */

def milliseconds(lst):
    result = 0
    result += lst[0] * 8.64 * 10 ** 7
    result += lst[1] * 3.6 * 10 ** 6
    result += lst[2] * 60000
    result += lst[3] * 1000

    return result

def str_to_int(txt):
    txt = txt.split(':')
    lst = []
    for item in txt:
        lst.append(int(item))
    
    return lst

entrance = input("\nIntroduzca una fecha de días, horas, minutos y segundos, separados por dos puntos (|:|:|:|): ")

result = milliseconds(str_to_int(entrance))
print(f"\nFecha en milisegundos: {result:.0f}")


