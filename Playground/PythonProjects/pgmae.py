#Load and show an image with Pillow
from PIL import Image

#Load the image
img = Image.open('unnamed.gif')

#Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

#show the image
img.show()