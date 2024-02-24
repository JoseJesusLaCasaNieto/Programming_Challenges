# /*
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
#  *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
#  *   interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */

def is_palindrome(word):
    return word == word[::-1]

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def is_isogram(word):
    return len(word) == len(set(word.lower()))

# Accessing specific characters
text = "Hello"
print("Accessing specific characters:")
print("First character:", text[0])
print("Last character:", text[-1])

# Substrings
print("\nSubstrings:")
print("Substring from index 1 to 3:", text[1:4])

# Length of the string
print("\nLength of the string:")
print("Length of text:", len(text))

# Concatenation
print("\nConcatenation:")
text2 = " World!"
print("Concatenated string:", text + text2)

# Repetition
print("\nRepetition:")
print("Repeated string:", text * 3)

# Iteration
print("\nIteration:")
for char in text:
    print(char)

# Conversion to uppercase and lowercase
print("\nConversion to uppercase and lowercase:")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Replacement
print("\nReplacement:")
print("Replacing 'l' with 'x':", text.replace('l', 'x'))

# Splitting and joining
print("\nSplitting and joining:")
words = "This is a sentence"
word_list = words.split()
print("Splitting into words:", word_list)
print("Joining words with '-' separator:", '-'.join(word_list))

# Interpolation
print("\nInterpolation:")
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Verification
print("\nVerification:")
print("Is 'Hello' alphanumeric?", text.isalnum())
print("Is '123' numeric?", '123'.isnumeric())

# Extra exercise
word1, word2 = input("\nIntroduzca dos palabras separadas por espacios (| |): ").split()

print(f"\n¿Son palíndromos?\n{word1}: {is_palindrome(word1)}\n{word2}: {is_palindrome(word2)}")
print(f"\n¿Son anagramas?\n{word1} y {word2}: {is_anagram(word1, word2)}")
print(f"\n¿Son isogramas?\n{word1}: {is_isogram(word1)}\n{word2}: {is_isogram(word2)}")







