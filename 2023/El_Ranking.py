# /*
#  * Todo llega a su fin... Este es el último reto de programación
#  * semanal de 2023.
#  *
#  * Crea un programa que muestre un listado calculado en tiempo real
#  * con todos los usuarios que han resuelto algún reto de programación
#  * de este año.
#  * - El listado debe estar ordenado por el número de ejercicios resueltos
#  *   por cada usuario (y mostrar ese contador al lado de su nombre).
#  * - También se debe de mostrar el número de usuarios que han participado
#  *   y el número de correcciones enviadas.
#  *
#  * Muchísimas gracias por ayudar a crear este gran recurso
#  * para la comunidad... ¡Prepárate para 2024!
#  */

import os

folder_path = os.path.dirname(__file__)
folder_path = os.path.abspath(os.path.join(folder_path, os.pardir, os.pardir))

users = {}
exercises = 0

for _, _, files in os.walk(folder_path):

    for file in files:
        if file.lower() not in ["ejercicio.md", "language_stats.py", ".ds_store", ".gitignore"]:
            user = os.path.splitext(file.lower())[0]
            users[user] = users.get(user, 0) + 1
            exercises += 1

sorted_users = sorted(users.items(), key=lambda item: item[1], reverse=True)

print(f"Número de usuarios únicos: {len(users)}")
print(f"Número de correcciones enviadas: {exercises}")
print("Ranking de usuarios y correcciones:")
for index, user in enumerate(sorted_users):
    print(f"{index + 1} {user[0]} ({user[1]})")







