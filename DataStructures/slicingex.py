name = ' Fahim Altamash Ansari'
fname = name[:5]
lname = name[-7:]
mname = name[6:-8]
print(fname, mname, lname)

#reversed
rev_name = name[::-1]
print(rev_name)

#middle name reversed
mname_rev = name[6:-8][::-1]
print(mname_rev)

#every index character
even_name = name[::2]
print(even_name)
#every odd index character
odd_name = name[1::2]
print(odd_name)