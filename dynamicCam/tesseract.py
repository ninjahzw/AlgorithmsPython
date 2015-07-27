try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
img = Image.open('ttt.jpg')
img.load()
img.split()

print(pytesseract.image_to_string(img))
