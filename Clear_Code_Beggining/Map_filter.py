my_list = [1,2,3,4,5,6,7,8,9,10]

"Map - changes valuses with a function inside of iterable"
print(list(map(lambda value: value**2,my_list)))

"Filter - filters out values from a condition"
print(list(filter(lambda value: value<5,my_list)))

"Excersise"
#convert both power and filter function into one list
print(list(map(lambda value: value**2,filter(lambda value: value<4,my_list))))
#or
print([num**2 for num in my_list if num<4])