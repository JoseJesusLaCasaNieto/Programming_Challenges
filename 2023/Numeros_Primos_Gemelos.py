# /*
#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  *
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)
#  */

def is_prime(number):
    """Function that checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_twin_prime_pairs(max_range):
    """Function that finds and displays pairs of twin prime numbers in a range."""
    twin_prime_pairs = []
    for number in range(2, max_range):
        if is_prime(number) and is_prime(number + 2):
            twin_prime_pairs.append((number, number + 2))

    return twin_prime_pairs

# Example of use
max_range = 14
pairs_found = find_twin_prime_pairs(max_range)

# Display the found pairs
print(f"Twin prime number pairs in the range up to {max_range}:")
for pair in pairs_found:
    print(pair)






