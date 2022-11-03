"Zbiory to wartości unikatowe"
list_1 = [1,1,2,3,4]
set = set(list_1)
print(set)

"Sets"
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7}
print(set_1.union(set_2))#Excatly the same as print(set_1|set_2)
print(set_1.intersection(set_2))
print(set_1.difference(set_2))