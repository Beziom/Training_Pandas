"Sorting by command"
list_0= [1,5,3,7,6,43,7,9,6,4,2,1]
list_0.sort()
# print(list) # [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 9, 43]
# print()

list_1 = [4,5,6,4,3,3,9]
# print(sorted(list_1,reverse = True))

"Using function in other functions"
list_2 = [("B", 3), ("C",10), ("A", 6), ("D", 7)]
# def sort_function(item):
#     return item[1] 
# print(sorted(list_2, key = sort_function))

"Different approach"
list_2 = [("B", 3), ("C",10), ("A", 6), ("D", 7)]
# print(sorted(list_2, key = lambda value: value[1]))

"Excersise"
#1. sort list by invontory numbers
#2. Sort list by lenght of inventory name
inventory_name = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95 ,421,23, 43]
combined = list(zip(inventory_name,inventory_numbers))
#1
print(sorted(combined,key = lambda number:number[1]))
#2
print(sorted(combined, key = lambda lenght:len(lenght[0])))
