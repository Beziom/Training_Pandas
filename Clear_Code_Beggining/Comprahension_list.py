"Normal Loop to create list from 0 to 99"
from numpy import number


my_list=[]
for num in range(0,100):
    my_list.append(num)

"List Comprahension"
my_list_2 = [f'is {num}' for num in range(0,100)] # example of list comprahension
my_list_3 = [(num,num,num)for num in range(0,100)]
my_list_4 = [num for num in range (0,100) if num < 50] # example of list comprahensiuon and if statement
my_list_5 = [(num,num,num) if num <50 else (0,0,0) for num in range(0,100)] # example of list comprahensiuon and if statement
# print(my_list_2)
# print(my_list_3)
# print(my_list_5)

inventory_name = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95 ,421,23, 43]

replenish_list = [(name,number) for name,number in zip(inventory_name, inventory_numbers) if number <50] # extended in python
# print(replenish_list)

"Combine list comptehension - repeating list"
combined_comp = [[x for x in range(5)] for y in range (10)] # repeating all lists by ten times (y)
# for index, row in enumerate(combined_comp):
#     # print(index,row)

"Example of map creating"
map = [[(x,y) for x in range(5)] for y in range(10)]
# for row in map:
#     print(row)

"Excersise - create fiels for chess board"
board = [[f'{letter}{num}' for num in range(1,9)]for letter in "ABCDEFGH"[::-1]]
for row in board:
    print(row)

"My own to create black and White Board"   
chess = [["W" if letter % 2 else "B" for letter in range(4)] for num in range (4)]
for row in chess:
    print(4*[row[0],row[1]])
    print(4*[row[1],row[0]])