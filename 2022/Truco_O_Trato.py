# /*
#  * Este es un reto especial por Halloween.
#  * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
#  * o Trato" y un listado (array) de personas con las siguientes propiedades:
#  * - Nombre de la niña o niño
#  * - Edad
#  * - Altura en centímetros
#  *
#  * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
#  * siguiendo estos criterios:
#  * - Un susto por cada 2 letras del nombre por persona
#  * - Dos sustos por cada edad que sea un número par
#  * - Tres sustos por cada 100 cm de altura entre todas las personas
#  * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
#  *
#  * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
#  * siguiendo estos criterios:
#  * - Un dulce por cada letra de nombre
#  * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
#  * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
#  * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
#  * - En caso contrario retornará un error.
#  */

import random

def trick_or_treat(action, kids):
    if action == "trick":
        return give_tricks(kids)
    elif action == "treat":
        return give_treats(kids)
    else:
        return "Error: Invalid action. Please choose 'trick' or 'treat'."

def give_tricks(kids):
    tricks = ""
    for kid in kids:
        # Calculate number of tricks based on name length
        tricks += "🎃" * (len(kid["name"]) // 2)
        # Calculate number of tricks based on age (two tricks per even age)
        tricks += "👻💀" * (kid["age"] // 2)
        # Calculate number of tricks based on height (three tricks per 100 cm)
        tricks += "🕷🕸🦇" * (kid["height"] // 100 // 3)
    return tricks

def give_treats(kids):
    treats = ""
    for kid in kids:
        # Calculate number of treats based on name length
        treats += "🍰🍬🍡🍭🍪🍫🧁🍩" * len(kid["name"])
        # Calculate number of treats based on age (one treat per 3 years up to 10 years)
        treats += "🍰🍬🍡🍭🍪🍫🧁🍩" * min(kid["age"] // 3, 10)
        # Calculate number of treats based on height (two treats per 50 cm up to 150 cm)
        treats += "🍰🍬🍡🍭🍪🍫🧁🍩" * min(kid["height"] // 50, 3)
    return treats

# Test the function
kids = [
    {"name": "Alice", "age": 8, "height": 120},
    {"name": "Bob", "age": 10, "height": 140},
    {"name": "Charlie", "age": 12, "height": 160}
]

print(trick_or_treat("trick", kids))
print(trick_or_treat("treat", kids))







