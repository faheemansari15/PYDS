# String validation

file = input("Enter file name: ")

if file.endswith(".png"):
    print("It's a png file")

elif file.endswith(".jpg"):
    print("It's a jpg file")

elif file.endswith(".docx"):
    print("It's a docx file")        

elif file.endswith(".py") or file.endswith(".ipynb"):
    print("It's a python file")

else:
    print("Unidentified file, destroy your system")       