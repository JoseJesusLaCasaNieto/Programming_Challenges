# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */

def find_pythagorean_triples(max_num):
    triples = []
    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            for c in range(b, max_num + 1):
                if a * a + b * b == c * c:
                    triples.append((a, b, c))
    return triples

max_num = int(input("Introduzca un número entero: "))

triples = find_pythagorean_triples(max_num)
print("\nNúmeros pitagóricos mayores que", max_num, ":", triples)








