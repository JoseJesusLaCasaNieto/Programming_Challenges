# /*
#  * Crea un juego interactivo por terminal en el que tendrás que adivinar
#  * el resultado de diferentes operaciones matemáticas aleatorias
#  * (suma, resta, multiplicación o división de dos números enteros).
#  * - Tendrás 3 segundos para responder correctamente.
#  * - El juego finaliza si no se logra responder en ese tiempo.
#  * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
#  * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
#  *   de la operación (cada vez en un operando):
#  *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#  *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#  *   - Preguntas 11 a 15: XX operación YY
#  *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#  *   ..
#  */

import random
import time

def generate_operation(num_digits):
    if num_digits == 1:
        return (random.randint(0, 9), random.randint(0, 9))
    elif num_digits == 2:
        return (random.randint(0, 99), random.randint(0, 9))
    elif num_digits == 3:
        return (random.randint(0, 99), random.randint(0, 99))
    else:
        return (random.randint(0, 999), random.randint(0, 99))

def play_game():
    score = 0
    digits = 1
    for _ in range(20):
        num1, num2 = generate_operation(digits)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '/':
            while num2 == 0:  # Avoid division by zero
                num2 = random.randint(0, 99)
        
        print(f"What is {num1} {operator} {num2}?")
        start_time = time.time()
        try:
            answer = float(input())
        except ValueError:
            print("Invalid input. Time's up!")
            break
        
        elapsed_time = time.time() - start_time
        if elapsed_time > 3:
            print("Time's up!")
            break
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

        if answer == result:
            score += 1
            if score % 5 == 0:
                digits += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print(f"Game over! Your score is {score}.")

play_game()





