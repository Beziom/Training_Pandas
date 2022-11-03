"Training"
set_comp = {num for num in range(10)}
dict_comp = {num:num2 for num,num2 in zip(range(1,101),range(100,200))}
tuple_comp = tuple((num for num in range(1,100)))
print(set_comp)
print()
print(dict_comp)
print()
print(tuple_comp)
print()

"Excersise"
dict_comp_1 = {num:[1,2,3,4,5] for num in "ABCDE"}
for key,value in dict_comp_1.items():
    print(key,value)