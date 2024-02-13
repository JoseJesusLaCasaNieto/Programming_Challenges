# /*
#  * Crea una función que sea capaz de detectar y retornar todos los
#  * handles de un texto usando solamente Expresiones Regulares.
#  * Debes crear una expresión regular para cada caso:
#  * - Handle usuario: Los que comienzan por "@"
#  * - Handle hashtag: Los que comienzan por "#"
#  * - Handle web: Los que comienzan por "www.", "http://", "https://"
#  *   y finalizan con un dominio (.com, .es...)
#  */

import re

def detect_handles(text):
    user_handles = re.findall(r'@(\w+)', text)
    hashtag_handles = re.findall(r'#(\w+)', text)
    web_handles = re.findall(r'(?:www\.|http://|https://)(?:[^\s]+)', text)
    return user_handles, hashtag_handles, web_handles

# Test the function
text = "Check out my new website www.example.com and follow me on @user1 and #python #coding"
print(text + "\n")
user_handles, hashtag_handles, web_handles = detect_handles(text)
print("User Handles:", user_handles)
print("Hashtag Handles:", hashtag_handles)
print("Web Handles:", web_handles)









