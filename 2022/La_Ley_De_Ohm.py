# /*
#  * Crea una función que calcule el valor del parámetro perdido
#  * correspondiente a la ley de Ohm.
#  * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#  *   el valor del tercero (redondeado a 2 decimales).
#  * - Si los parámetros son incorrectos o insuficientes, la función retornará
#  *   la cadena de texto "Invalid values".
#  */

def ohms_law(V=None, R=None, I=None):
    if V is None:
        if R is None or I is None:
            return "Invalid values"
        else:
            return round(R * I, 2)
    elif R is None:
        if V is None or I is None:
            return "Invalid values"
        else:
            return round(V / I, 2)
    elif I is None:
        if V is None or R is None:
            return "Invalid values"
        else:
            return round(V / R, 2)
    else:
        return "Invalid values"

# Example usage:
print(ohms_law(V=12, R=4))  # Should print 3.0
print(ohms_law(V=12, I=3))  # Should print 4.0
print(ohms_law(R=4, I=2))   # Should print 8.0
print(ohms_law(V=12))        # Should print "Invalid values"
print(ohms_law(I=3))         # Should print "Invalid values"
print(ohms_law())            # Should print "Invalid values"







