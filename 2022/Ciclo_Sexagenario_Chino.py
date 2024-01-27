# /*
#  * Crea un función, que dado un año, indique el elemento 
#  * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
#  * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
#  * - El ciclo sexagenario se corresponde con la combinación de los elementos
#  *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
#  *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
#  *   (en este orden).
#  * - Cada elemento se repite dos años seguidos.
#  * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
#  */

def chinese_zodiac_sexagenary_cycle(year):
    elements = ['madera', 'fuego', 'tierra', 'metal', 'agua']
    animals = ['rata', 'buey', 'tigre', 'conejo', 'dragón', 'serpiente',
               'caballo', 'oveja', 'mono', 'gallo', 'perro', 'cerdo']

    index = (year - 1984) % 60

    element_index = (index // 2) % 5
    animal_index = index % 12

    return elements[element_index], animals[animal_index]

year = int(input("Introduzca un año, desde 1984 hasta 2044: "))

element, animal = chinese_zodiac_sexagenary_cycle(year)
print(f"El año {year}, se corresponde con el elemento {element} y el animal {animal}.")






