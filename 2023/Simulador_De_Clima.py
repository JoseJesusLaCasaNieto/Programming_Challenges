# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */

import random

def weather_simulation(initial_temp, initial_rain_prob, num_days):
    temperature = initial_temp
    rain_probability = initial_rain_prob
    total_rainy_days = 0
    temperatures = []

    for _ in range(num_days):
        temperatures.append(temperature)

        if random.random() < 0.1:
            temperature += random.choice([-2, 2])

        if temperature > 25:
            rain_probability += 0.2

        if temperature < 5:
            rain_probability -= 0.2

        if random.random() < rain_probability:
            temperature -= 1
            total_rainy_days += 1

    max_temp = max(temperatures)
    min_temp = min(temperatures)

    print("Temperature predictions:")
    for day, temp in enumerate(temperatures, 1):
        print(f"Day {day}: {temp}°C")

    print(f"\nMaximum temperature: {max_temp}°C")
    print(f"Minimum temperature: {min_temp}°C")
    print(f"Total rainy days: {total_rainy_days}")

# Example usage:
initial_temp = float(input("Enter initial temperature (in °C): "))
initial_rain_prob = float(input("Enter initial rain probability (0 to 1): "))
num_days = int(input("Enter number of days for prediction: "))

weather_simulation(initial_temp, initial_rain_prob, num_days)








