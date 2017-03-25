# -*- coding: utf-8 -*-
#
import random,string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def CreateValidateCode():
    width,height = 120,30
    bgcolor = (255,255,255)
    fontcolor = (0,0,255)
    font_size = 18 

    lowercase = string.lowercase
    uppercase = string.uppercase 
    numbers = string.digits
    all_chars = ''.join((lowercase,uppercase,numbers))
    random_code = ''.join(random.sample(all_chars,4))


    image = Image.new('RGBA',(width,height),bgcolor)
    font = ImageFont.truetype("/System/Library/Fonts/AquaKana.ttc",font_size)
    draw = ImageDraw.Draw(image)
    font_width, font_height = font.getsize(random_code)
    draw.text(((width - font_width) / 4, (height - font_height) / 4),random_code,font=font,fill=fontcolor)
    image.save('idencode.png')

if __name__ == "__main__":
    CreateValidateCode()

