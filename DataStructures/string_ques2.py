# wap to find all the occurance of a word in a string and display its index
# ex->> "this is that and that is this, that is that and this is this"

# from string import ascii_lowercase

msg = "this is that and that is this, that is that and this is this"
start = 0
query = "that"

'''for char in msg:
    occ = msg.count("a")
    print("a", occ)
    print("Index:", msg.index("a"))
    break'''

while True:
    index = msg.find(query, start)
    if index == -1:
        break
    print(f"{query} at {index}")
    start = index + 1