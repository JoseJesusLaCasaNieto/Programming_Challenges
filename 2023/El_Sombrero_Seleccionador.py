# /*
#  * Crea un programa que simule el comportamiento del sombrero selccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts:
#  *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#  *   y crear el algoritmo seleccionador:
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */

gryffindor = 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0

entrance_1 = input("¿Cuál de las siguientes opciones odiaría más que la gente te llamara? (Ordinario, Ignorante, Cobarde, Egoista): ")
entrance_1 = entrance_1.lower()

if entrance_1 == 'ordinario':
    ravenclaw += 1
elif entrance_1 == 'ignorante':
    hufflepuff += 1
elif entrance_1 == 'cobarde':
    slytherin += 1
else:
    gryffindor += 1

entrance_2 = input("\nPreferirías inventar una poción que garantizara: Gloria, Sabiduria, Amor, Poder. ")
entrance_2 = entrance_2.lower()

if entrance_1 == 'gloria':
    ravenclaw += 1
elif entrance_1 == 'sabiduria':
    hufflepuff += 1
elif entrance_1 == 'poder':
    slytherin += 1
else:
    gryffindor += 1

entrance_3 = input("\n¿Cómo te gustaría ser conocido en la historia? (Sabio, Bueno, Grande, Audaz): ")
entrance_3 = entrance_3.lower()

if entrance_1 == 'grande':
    ravenclaw += 1
elif entrance_1 == 'sabio':
    hufflepuff += 1
elif entrance_1 == 'audaz':
    slytherin += 1
else:
    gryffindor += 1

entrance_4 = input("\n¿Qué tipo de instrumento agrada más a tu oído? (Violin, Tambores, Piano, Trompeta): ")
entrance_4 = entrance_4.lower()

if entrance_1 == 'trompeta':
    ravenclaw += 1
elif entrance_1 == 'piano':
    hufflepuff += 1
elif entrance_1 == 'tambores':
    slytherin += 1
else:
    gryffindor += 1

entrance_5 = input("\n¿Cuál preferirías ser? (Querido, Imitado, Alabado, Envidiado): ")
entrance_5 = entrance_5.lower()

if entrance_1 == 'querido':
    ravenclaw += 1
elif entrance_1 == 'alabado':
    hufflepuff += 1
elif entrance_1 == 'envidiado':
    slytherin += 1
else:
    gryffindor += 1

results = {'Ravenclaw': ravenclaw, 'Gryffindor': gryffindor, 'Slytherin': slytherin, 'Hufflepuff': hufflepuff}
winner = max(results, key= lambda k: results[k])
print("\nResultado del Sombrero Seleccionador: {}".format(winner))


