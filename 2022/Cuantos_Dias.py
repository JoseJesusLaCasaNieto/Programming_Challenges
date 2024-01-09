# /*
#  * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
#  * de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se
#  *   lanzará una excepción.
#  */

from datetime import datetime

entrance1, entrance2 = input("Introduzca dos fechas con formato dd/MM/yyyy separadas por un espacio (| |): ").split()

def diff_between_days(date1, date2):
    try:
        date1_obj = datetime.strptime(date1, "%d/%m/%Y")
        date2_obj = datetime.strptime(date2, "%d/%m/%Y")

        abs_diff = abs((date1_obj - date2_obj).days)

        return abs_diff

    except ValueError:
        raise ValueError("Una de las fechas no es válida. Utiliza el formato 'dd/MM/yyyy'.")

print(f"La diferencia en días entre {entrance1} y {entrance2} es de {diff_between_days(entrance1, entrance2)} días.")




