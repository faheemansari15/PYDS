# Task count the occurance of all vowels in a string

msg = input("Enter a sentence")

# a
print("a are: ", msg.count("a"))

# e
print("e are: ", msg.count("e"))

# i
print("i are: ", msg.count("i"))

# o
print("o are: ", msg.count("o"))

# u
print("u are: ", msg.count("u"))


for vowel in "aeiou":
    print(vowel, msg.lower().count(vowel))
    print(f"{vowel} counted {msg.lower().count(vowel)} times")