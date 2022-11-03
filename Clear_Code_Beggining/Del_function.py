#remove items from a lst
a= [1,2,3,4]
del a[0]
print(a)

#remove item by value
a.remove(4)
print(a)

#pop - by the negative
print(a.pop(-1)) # value can be printed
print(a)

#clear - clear entire list
a.clear()
print(a)