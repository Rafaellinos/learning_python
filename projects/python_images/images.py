"""
pip3 install Pillow
"""
from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
print(img.format, img.size, img.mode) # JPEG (640, 640) RGB

filtered_img = img.filter(ImageFilter.SHARPEN) # .BLUR, SMOOTH

filtered_img.save("blur.png", 'png') # filename, format. Change to png to suport those filters

#############

img = Image.open('./pokedex/squirtle.jpg')

gray_img = img.convert('L') # convert to gray
gray_img = gray_img.rotate(180)
#gray_img = gray_img.resize((300, 300))
gray_img.thumbnail((400, 200)) # instead of using resize, to keep its proportion and aspect ration
box = (100, 100, 400, 400)
gray_img = gray_img.crop(box) # cut the picture based on the box
gray_img.save("./new/gray.png", 'png')
gray_img.show() # opens the img

