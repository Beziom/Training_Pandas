"Indexing in dictionary"
dict_1 = {1:"A", 2:"B", 3:"C"}
print(dict_1[1])
print(dict_1.get(1)) #get() unction doesn't crash
dict_1.update({4:"D"})#adding something to dict
dict_1[5] = "E"
print(dict_1)