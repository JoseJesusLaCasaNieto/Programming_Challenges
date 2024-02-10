# /*
#  * Crea un función que reciba un texto y retorne la vocal que
#  * más veces se repita.
#  * - Ten cuidado con algunos casos especiales.
#  * - Si no hay vocales podrá devolver vacío.
#  */

def most_repeated_vowel(text):
    dct = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Count occurrences of vowels in the text
    for letter in text:
        if letter.lower() in dct:
            dct[letter.lower()] += 1
    
    # Find the most repeated vowel
    max_repetitions = max(dct.values())
    if max_repetitions == 0:
        return "Vacío"
    else:
        most_repeated_vowel = [key for key, value in dct.items() if value == max_repetitions][0]
        return most_repeated_vowel

# Ask user for text input
text = input("Introduzca un texto: ")

# Calculate and display the most repeated vowel
result = most_repeated_vowel(text)
print(f"\nLa vocal más repetida es: {result}")












