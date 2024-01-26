# /*
#  * Como cada año, el día 256 se celebra el "Día de la Programación".
#  * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
#  * 256 regalos para seguir aprendiendo programación:
#  * https://diadelaprogramacion.com
#  *
#  * Para seguir ayudando, te propongo este reto:
#  * Mostrar la sintaxis de los principales elementos de un lenguaje
#  * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
#  *
#  * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
#  * y comenta cada bloque para identificar con qué se corresponde:
#  * - Haz un "Hola, mundo!"
#  * - Crea variables de tipo String, numéricas (enteras y decimales)
#  *   y Booleanas (o cualquier tipo de dato primitivo).
#  * - Crea una constante.
#  * - Usa un if, else if y else.
#  * - Crea estructuras como un array, lista, tupla, set y diccionario.
#  * - Usa un for, foreach y un while.
#  * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
#  * - Crea una clase.
#  * - Muestra el control de excepciones.
#  *
#  * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
#  * de sintaxis básica de muchos lenguajes.
#  *
#  * ¡Muchas gracias!
#  */

# Hola mundo.
print("Hola, mundo!\n")

# Variables.
name = 'Nombre'
int_number = int(5)
float_number = float(5)
boolean = bool(1)

print(name, type(name))
print(int_number, type(int_number))
print(float_number, type(float_number))
print(boolean, type(boolean))

# Constantes.
PI = 3.14159
print("\nValor de PI:", PI)

# Condiciones.
n = int(input("\nIntroduzca un número entero: "))
print(f"\nn = {n}")
if n < 10:
    print("n es menor que 10.")
elif n > 10:
    print("n es mayor que 10.")
else:
    print("n es igual que 10")

# Estructuras.
array = [1, 2, 3]
lista = [4, 5, 6]
tupla = (7, 8, 9)
conjunto = {10, 11, 12}
diccionario = {'a': 13, 'b': 14, 'c': 15}

print("\nArray:", array)
print("Lista:", lista)
print("Tupla:", tupla)
print("Conjunto:", conjunto)
print("Diccionario:", diccionario)

# Bucles.
# Bucles
print("\nFor:")
for i in range(5):
    print(i, end=' ')

print("\nWhile:")
count = 0
while count < 3:
    print(count, end=' ')
    count += 1

# Funciones.
def funcion_sin_parametros():
    print("\n\nEsta es una función sin parámetros.")

def funcion_con_parametro(parametro):
    print(f"Esta es una función con el parámetro: {parametro}.")

def suma(a, b):
    return a + b

funcion_sin_parametros()
funcion_con_parametro("Hola")
resultado = suma(3, 4)
print(f"Resultado de la suma: {resultado}")

# Clase.
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

objeto = MiClase("Ejemplo")
print("\nNombre de la clase:", objeto.obtener_nombre())

# Control de excepciones.
try:
    resultado_division = 10 / 0
except ZeroDivisionError:
    print("\n¡Error! División por cero.")
finally:
    print("Esta parte se ejecuta siempre.")








