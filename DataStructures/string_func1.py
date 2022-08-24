msg = "journey before Destination"

# formatting function

print("Uppercase: ", msg.upper())
print("Lowercase: ", msg.lower())
print("Titlecase: ", msg.title())

print("title: ", msg.capitalize())
print("title: ", msg.swapcase())
print("title: ", msg.casefold()) # same as lower

print("Original: ", msg)
msg = msg.upper() # Updating the msg variable to store upper cased string
print("Updated: ", msg)