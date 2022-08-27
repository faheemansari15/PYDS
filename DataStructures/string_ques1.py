# wap to count all the alphabets in a string
# and display the output like
# a - 3
# b - 9
# ...
# z - 0

from string import ascii_lowercase

msg = "Life Before Death, Hope Before Despair, Journey Before Destination"
for char in ascii_lowercase:
    print(f"{char} - {msg.count(char)}")