from PIL import Image, ImageFilter, ImageEnhance # 2 classes added

im = Image.open("images\imagepro.jpeg") # relative address
im2 = Image.open(r"C:\Users\User\Documents\PYDS\images\imagepro2.jfif") # absolute address

'''im.filter(ImageFilter.EMBOSS).show()
im.filter(ImageFilter.CONTOUR).show()
im.filter(ImageFilter.FIND_EDGES).show()
im.filter(ImageFilter.BLUR).show()
im.filter(ImageFilter.SHARPEN).show()
im.filter(ImageFilter.SMOOTH).show()
im.filter(ImageFilter.MaxFilter(3)).show() # highlight whites
im.filter(ImageFilter.MinFilter(3)).show() # highlight blacks
im.filter(ImageFilter.MedianFilter(5)).show() # highlight greys
im.filter(ImageFilter.GaussianBlur(100)).show()'''

# eim = ImageEnhance.Color(im)
# for i in range(10,12,5):
    # eim.enhance(i).show() 

imc = im.copy()
im2_s = im2.resize((200,100))
imc.paste(im2_s, (20,10))
imc.paste(im2_s, (200,100))
imc.show() 