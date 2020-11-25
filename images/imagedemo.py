from PIL import Image, ImageFilter, ImageDraw
import numpy
import PIL

harishImage = PIL.Image.open("Harish.jpg")
print(harishImage)
blurred = harishImage.filter(ImageFilter.BLUR)

grayScaleImage = harishImage.convert('L')
# grayScaleImage.show()

croppedImage = harishImage.crop((0, 0, 700, 700))
# croppedImage.show()

rotatedImage = harishImage.rotate(180)
# rotatedImage.show()

pixdata = harishImage.load()
for y in range(harishImage.size[1]):
    for x in range(harishImage.size[0]):
        #print(x,y , pixdata[x, y])
        if pixdata[x, y][0]<=10 and pixdata[x, y][1]<=10 and pixdata[x, y][2]<=10:
            #print(pixdata[x,y])
            pixdata[x, y] = (200, 200, 50)
            harishImage.putpixel((x,y),pixdata[x, y])

# harishImage.show()

# pixelData = set(harishImage.getdata())
# for i in pixelData:
#     print(i)

drawImage = ImageDraw.Draw(harishImage)
drawImage.line((0, 0) + harishImage.size, fill=128,width=10)
drawImage.line((0, harishImage.size[1], harishImage.size[0], 0), fill=128,width=10)
harishImage.show()


