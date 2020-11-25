from PIL import Image, ImageFilter, ImageDraw
import numpy
import PIL

harishImage = PIL.Image.open("Harish.jpg")
drawImage = ImageDraw.Draw(harishImage)
drawImage.line((0, 0) + harishImage.size, fill=128, width=10)
drawImage.line((0, harishImage.size[1], harishImage.size[0], 0), fill=128, width=10)
# harishImage.show()

drawImage.arc([(0, 0), (800, 1000)],30,60,fill ="green",width=10)
harishImage.show()