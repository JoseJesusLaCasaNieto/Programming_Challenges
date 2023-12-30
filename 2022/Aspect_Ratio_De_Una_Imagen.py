# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo:
#  *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */

from PIL import Image
import requests
from io import BytesIO

entrance = input("Introduzca la URL de la imagen: ")
download_request = requests.get(entrance)

if download_request.status_code == 200:
    download_image = Image.open(BytesIO(download_request.content))
    width, height = download_image.size
    aspect_ratio = width / height
    print("Aspect Ratio: {}".format(aspect_ratio))
else:
    print("\nNo se pudo descargar la imagen desde la URL.")

# print(f"Código de respuesta HTML: {download_request.status_code}")



