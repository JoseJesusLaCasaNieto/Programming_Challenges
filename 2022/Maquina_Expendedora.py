# /*
#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas
#  *   de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#  */

def change_coins(AMOUNT, SYSTEM):    # Aplicación de técnica voraz para la devolución del dinero.
    SOLUTION = [0] * len(SYSTEM)
    AccumulatedValue = 0

    for i, value in enumerate(SYSTEM):
        coins = (AMOUNT - AccumulatedValue) // value
        SOLUTION[i] = coins
        AccumulatedValue = AccumulatedValue + coins * value

        if AMOUNT == AccumulatedValue:
            return SOLUTION

    print("No se puede encontrar una solución.")

def vending_machine(product_code, amount, system):
    products = {
        1: {"name": "Producto1", "price": 150},
        2: {"name": "Producto2", "price": 100},
        3: {"name": "Producto3", "price": 200},
    }

    if product_code not in products:
        print("Producto no válido. Devolviendo el dinero.")
        return system

    product_price = products[product_code]["price"]

    if amount < product_price:
        print("Dinero insuficiente. Devolviendo el dinero.")
        return system

    change = change_coins(amount - product_price, system)

    print(f"\nProducto: {products[product_code]['name']}")
    print("Cambio:", dict(zip(system, change)))

products = {
    1: {"name": "Producto1", "price": 150},
    2: {"name": "Producto2", "price": 100},
    3: {"name": "Producto3", "price": 200},
}
print(products)

entrance = input("Introduzca el número del producto y la cantidad a ingresar, separados por un espacio (| |): ").split()
product_code = int(entrance[0])
amount = int(entrance[1])

system = [200, 100, 50, 20, 10, 5, 2, 1]

vending_machine(product_code, amount, system)







