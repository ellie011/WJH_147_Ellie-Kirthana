import os 
from PIL import Image, ImageDraw, ImageFont #import the images used
filename='logo.png'
logos = Image.open(filename, 'r')
filename1='1.png'
bg = Image.open(filename1, 'r')
#lines 5-7 opening logo and image document
text_img = Image.new('RGBA', (1000, 1200), (0, 0, 0, 0))
text_img.paste(bg, (0,0)) #9 resizes phne and 10 centers image
text_img.paste(logos, (340, 675), mask=logos) #mask the two images on top of each other
text_img.save("phonee.png", format="png")
#save the modified final product
