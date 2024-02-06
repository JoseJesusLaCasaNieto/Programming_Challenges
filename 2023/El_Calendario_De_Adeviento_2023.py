# /*
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#  */

import random

participants = []

def add_participant(name):
    if name in participants:
        print("\nParticipant already exists.")
    else:
        participants.append(name)
        print(f"\nParticipant {name} added.")

def show_participants():
    print("\nParticipants:")
    for participant in participants:
        print(participant)

def remove_participant(name):
    if name in participants:
        participants.remove(name)
        print(f"\nParticipant {name} removed.")
    else:
        print("\nParticipant not found.")

def draw_winner():
    if participants:
        winner = random.choice(participants)
        participants.remove(winner)
        print(f"\nThe winner is: {winner}")
    else:
        print("\nNo participants to draw from.")

while True:
    print("\nMenu:")
    print("1. Add participant")
    print("2. Show participants")
    print("3. Remove participant")
    print("4. Draw winner")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter participant name: ")
        add_participant(name)
    elif choice == "2":
        show_participants()
    elif choice == "3":
        name = input("Enter participant name to remove: ")
        remove_participant(name)
    elif choice == "4":
        draw_winner()
    elif choice == "5":
        print("\nQuitting program.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")








