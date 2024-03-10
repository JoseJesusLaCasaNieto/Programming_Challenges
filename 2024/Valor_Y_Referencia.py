# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

# Asignación de variables por valor
x = 10
y = x  # Se asigna el valor de x a y
y = 20  # Cambiando el valor de y, x no se ve afectado
print(x)  # Output: 10

# Asignación de variables por referencia (en el caso de listas)
lista_1 = [1, 2, 3]
lista_2 = lista_1  # Se asigna la referencia de lista_1 a lista_2
lista_2.append(4)  # Modificando lista_2, lista_1 también se ve afectado
print(lista_1)  # Output: [1, 2, 3, 4]

# Función que recibe un parámetro por valor
def modificar_valor(valor):
    valor += 10
    print("Valor dentro de la función:", valor)

x = 5
modificar_valor(x)  # Llamando a la función con x
print("Valor fuera de la función:", x)  # Output: 5 (x no se modifica)

# Función que recibe un parámetro por referencia
def modificar_lista(lista):
    lista.append(4)
    print("Lista dentro de la función:", lista)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)  # Llamando a la función con mi_lista
print("Lista fuera de la función:", mi_lista)  # Output: [1, 2, 3, 4] (mi_lista se modifica)

def intercambiar_valor(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20

x, y = intercambiar_valor(x, y)
print("Valores originales:", 10, 20)
print("Valores intercambiados:", x, y)

def intercambiar_lista(lista1, lista2):
    lista1[:], lista2[:] = lista2[:], lista1[:]
    return lista1, lista2

mi_lista = [1, 2, 3]
otra_lista = [4, 5, 6]

mi_lista, otra_lista = intercambiar_lista(mi_lista, otra_lista)
print("Listas originales:", [1, 2, 3], [4, 5, 6])
print("Listas intercambiadas:", mi_lista, otra_lista)






