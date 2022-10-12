from PIL import Image

im = Image.open("imagepro.jpeg") # relative address
im2 = Image.open(r"C:\Users\User\Documents\PYDS\imagepro2.jfif") # absolute address

print(im)
print(im2) 

im.rotate(45).show()
im2.rotate(90).show() 