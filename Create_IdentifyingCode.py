# -*- coding: utf-8 -*-
#
import random,string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

__author__ = atiger77

'''
第一版简单实现验证码生成，明天把代码做下模块化
'''

def CreateValidateCode():
    width,height = 120,30   #图片长度，宽度
    bgcolor = (255,255,255) #背景
    fontcolor = (0,0,255)   #字体颜色
    font_size = 18          #字体大小
    
    #生成随机4位验证码
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

