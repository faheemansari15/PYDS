from PIL import Image, ImageDraw, ImageFont # 2 classes added help to draw on image

im = Image.open("images\imagepro.jpeg") # relative address
im2 = Image.open(r"C:\Users\User\Documents\PYDS\images\imagepro2.jfif") # absolute address

font = ImageFont.truetype(r"C:\Windows\Fonts\BOD_CR.TTF", 100) 
font2 = ImageFont.truetype(r"C:\Windows\Fonts\BKANT.TTF", 50)

imd = ImageDraw.Draw(im)

imd.text((20,100), "Eye", fill = (255,150,0), font = font, )
imd.text((500,600), "Price", fill = (0,0,0), font = font)
im.save("imagepros.jpeg") 