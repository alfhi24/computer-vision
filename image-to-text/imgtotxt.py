from PIL import Image
from pytesseract import image_to_string

img = Image.open("image.png")

text = image_to_string(img)
print(text)