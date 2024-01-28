# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

rgb = (0, 0, 0)
hexadecimal = "#000000"

print("RGB to HEX:", rgb_to_hex(*rgb))
print("HEX to RGB:", hex_to_rgb(hexadecimal))






