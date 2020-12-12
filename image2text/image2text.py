import pytesseract
from PIL import Image
img = Image.open('IMG_1408.JPG')
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img)    
print(result)