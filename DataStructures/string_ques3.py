# wap to remove all the punctuations from the string

from string import punctuation

msg = "fahe@@##&^e*(){}m:"
for p in punctuation:
    msg = msg.replace(p,"")
print(msg)    