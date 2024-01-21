# /*
#  * Crea un programa que determine si dos vectores son ortogonales.
#  * - Los dos array deben tener la misma longitud.
#  * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
#  */

def are_orthogonal(vector1, vector2):
    if len(vector1) != len(vector2):
        return False

    dot_product = sum(x * y for x, y in zip(vector1, vector2))

    return dot_product == 0

vector_a = [1, -2]
vector_b = [2, 1]

if are_orthogonal(vector_a, vector_b):
    print("The vectors are orthogonal.")
else:
    print("The vectors are not orthogonal.")







