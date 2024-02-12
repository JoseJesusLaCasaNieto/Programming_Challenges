# /*
#  * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
#  * ciencia y tecnología desde el 1 de diciembre.
#  *
#  * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
#  * lo siguiente:
#  * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
#  *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
#  * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
#  * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
#  *
#  * Notas:
#  * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
#  *   y finaliza a las 23:59:59.
#  * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
#  *   y segundos.
#  */

from datetime import datetime

def advent_calendar(date_obj):
    # Defining the advent calendar dates and corresponding gifts
    advent_dates = {
        datetime(2022, 12, 1): "Gift 1",
        datetime(2022, 12, 2): "Gift 2",
        datetime(2022, 12, 3): "Gift 3",
        datetime(2022, 12, 4): "Gift 4",
        datetime(2022, 12, 5): "Gift 5",
        datetime(2022, 12, 6): "Gift 6",
        datetime(2022, 12, 7): "Gift 7",
        datetime(2022, 12, 8): "Gift 8",
        datetime(2022, 12, 9): "Gift 9",
        datetime(2022, 12, 10): "Gift 10",
        datetime(2022, 12, 11): "Gift 11",
        datetime(2022, 12, 12): "Gift 12",
        datetime(2022, 12, 13): "Gift 13",
        datetime(2022, 12, 14): "Gift 14",
        datetime(2022, 12, 15): "Gift 15",
        datetime(2022, 12, 16): "Gift 16",
        datetime(2022, 12, 17): "Gift 17",
        datetime(2022, 12, 18): "Gift 18",
        datetime(2022, 12, 19): "Gift 19",
        datetime(2022, 12, 20): "Gift 20",
        datetime(2022, 12, 21): "Gift 21",
        datetime(2022, 12, 22): "Gift 22",
        datetime(2022, 12, 23): "Gift 23",
        datetime(2022, 12, 24): "Gift 24"
    }
    
    # Checking if the date is in the advent calendar
    if date_obj in advent_dates:
        gift = advent_dates[date_obj]
        remaining_time = datetime(2022, 12, 24, 23, 59, 59) - date_obj
        return f"On {date_obj.strftime('%Y-%m-%d')}, your gift is {gift}, and there are {abs(remaining_time.days)} days, {abs(remaining_time.seconds // 3600)} hours, {abs(remaining_time.seconds % 3600 // 60)} minutes, and {abs(remaining_time.seconds % 60)} seconds left until the end of the advent calendar."
    
    # Checking if the date is before the advent calendar starts6
    elif date_obj < datetime(2022, 12, 1):
        time_until_start = datetime(2022, 12, 1) - date_obj
        return f"It's {abs(time_until_start.days)} days, {abs(time_until_start.seconds // 3600)} hours, {abs(time_until_start.seconds % 3600 // 60)} minutes, and {abs(time_until_start.seconds % 60)} seconds until the advent calendar begins."
    
    # The date is after the advent calendar ends
    else:
        time_since_end = date_obj - datetime(2022, 12, 24, 23, 59, 59)
        return f"It's been {abs(time_since_end.days)} days, {abs(time_since_end.seconds // 3600)} hours, {abs(time_since_end.seconds % 3600 // 60)} minutes, and {abs(time_since_end.seconds % 60)} seconds since the advent calendar ended."

# Testing the function
test_date = datetime(2022, 12, 15)
print(advent_calendar(test_date))

test_date = datetime(2023, 12, 15)
print(advent_calendar(test_date))

test_date = datetime(2022, 10, 15, 12, 0, 0)
print(advent_calendar(test_date))








