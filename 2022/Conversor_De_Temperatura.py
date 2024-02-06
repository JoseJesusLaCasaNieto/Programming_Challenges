# /*
#  * Crea una función que transforme grados Celsius en Fahrenheit
#  * y viceversa.
#  *
#  * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#  *   y su unidad ("C" o "F").
#  * - En caso contrario retornará un error.
#  */

def convert_temperature(temperature):
    if "°" not in temperature or len(temperature) < 2:
        return "Error: Incorrect input format. It should include the symbol '°' followed by 'C' or 'F'."

    unit = temperature[-1]
    value = temperature[:-2]

    try:
        value = float(value)
    except ValueError:
        return "Error: Invalid temperature value."

    if unit == "C":
        fahrenheit = (value * 9/5) + 32
        return f"{value}°C is {fahrenheit}°F"
    elif unit == "F":
        celsius = (value - 32) * 5/9
        return f"{value}°F is {celsius}°C"
    else:
        return "Error: Unrecognized temperature unit. It should be 'C' or 'F'."

print(convert_temperature("25°C"))
print(convert_temperature("77°F"))
print(convert_temperature("30K"))
print(convert_temperature("30"))
print(convert_temperature("30°K"))







