# wap to remove all the punctuations from the string

from string import punctuation

'''msg = "fahe@@##&^e*():;{}m"
for p in punctuation:
    msg = msg.replace(p, "")
print(msg)'''   


msg2 = "an$#%s*&(ar@i)(*\)"
b = ""
for i in msg2:
    if i.isalpha():
        b += i
print(b)         