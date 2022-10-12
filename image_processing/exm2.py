from PIL import Image

im = Image.open("images\imagepro.jpeg") # relative address
im2 = Image.open(r"C:\Users\User\Documents\PYDS\images\imagepro2.jfif") # absolute address

print("resolution", im.size)
print("height", im.height)
print("width", im.width)
print("mode", im.mode)
print("format", im.format)
print("exif", im.info) 

im.convert("L").show()
im.resize((100,100)).show()
im.resize((2000,2000)).show()
im.resize((im.width * 5, im.height *5)).save("images\imagepro.jpeg") 