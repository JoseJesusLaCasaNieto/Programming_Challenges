# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */

# Function without parameters or return
def greet():
    print("Hello!")

# Function with one parameter and return
def square(x):
    return x * x

# Function with multiple parameters and return
def add(x, y):
    return x + y

# Function with local variable
def local_variable_example():
    x = 10
    print("Inside the function, x is:", x)

# Function with global variable
global_var = 20

def global_variable_example():
    print("Inside the function, global_var is:", global_var)

# Function inside another function
def outer_function():
    def inner_function():
        print("Inside inner function")
    inner_function()

# Using a built-in function
print("Absolute value of -5:", abs(-5))

# Testing all the functions
greet()
print("Square of 5:", square(5))
print("Addition of 3 and 4:", add(3, 4))
local_variable_example()
print("Outside the function, x is still:", global_var)
global_variable_example()
outer_function()

# Extra difficulty optional function
def print_numbers_and_return_count(text1, text2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
            count += 1
        elif i % 3 == 0:
            print(text1)
            count += 1
        elif i % 5 == 0:
            print(text2)
            count += 1
        else:
            print(i)
    return count

print("Number of times printed:", print_numbers_and_return_count("Fizz", "Buzz"))








