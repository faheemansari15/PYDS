# String validation function

value = input("Enter Any String")

# test
if value.isnumeric():
    print("Only Numbers: ", value.isnumeric())
if value.isalpha():
    print("Only Alphabets: ", value.isalpha())
if value.isalnum():
    print("Alphabets and Numbers: ", value.isalnum())
if value.isspace():
    print("Only Spaces", value.isspace())
if value.isupper():
    print("Uppercase Alphabets: ", value.isupper())
if value.islower():
    print("Lowercase Alphabets: ", value.islower()) 