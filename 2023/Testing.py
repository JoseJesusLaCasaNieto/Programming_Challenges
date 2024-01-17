# /*
#  * Crea tres test sobre el reto 12: "Viernes 13".
#  * - Puedes copiar una solución ya creada por otro usuario en
#  *   el lenguaje que estés utilizando.
#  * - Debes emplear un mecanismo de ejecución de test que posea
#  *   el lenguaje de programación que hayas seleccionado.
#  * - Los tres test deben de funcionar y comprobar
#  *   diferentes situaciones (a tu elección).
#  */

import unittest
import calendar

def friday_13(year, month):
    try:
        return calendar.weekday(year, month, 13) == 4
    except:
        return False

class TestFriday13(unittest.TestCase):

    def test_friday_13_true_date(self):
        self.assertTrue(friday_13(2023, 1))

    def test_friday_13_false_date(self):
        self.assertFalse(friday_13(2023, 3))

    def test_friday_13_invalid_year(self):
        self.assertFalse(friday_13("2023", 1))
        self.assertFalse(friday_13("MoureDev", 1))
        self.assertFalse(friday_13(-2023, 1))

    def test_friday_13_invalid_month(self):
        self.assertFalse(friday_13(2023, "1"))
        self.assertFalse(friday_13(2023, "one"))
        self.assertFalse(friday_13(2023, -1))

    def test_friday_13_invalid_data(self):
        self.assertFalse(friday_13("Brais", "Moure"))

if __name__ == '__main__':
    unittest.main()






