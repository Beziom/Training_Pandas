#Zip
inventory_name = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95 ,421,23, 43]

for name,number in zip(inventory_name,inventory_numbers):
    print(f'{name} current inventory is: {number}')

#Enumerate function = get the current index
print("How enumerate works: print(dict(enumerate(inventory_name)))\n")
print(dict(enumerate(inventory_name))) # [(0, 'Screws'), (1, 'Wheels'), (2, 'Metal parts'), (3, 'Rubber bits'), (4, 'Screwdrivers'), (5, 'Wood')]
print("Loop for with enumerate\n")
for index, thing in enumerate(inventory_name):
    print(f'{index}: {thing}')
    if index == len(inventory_name) //2: # 6//2 then 3 arguments will be calculated
        print("Halway done")
print()
for index,inventory_tuple in enumerate(zip(inventory_name,inventory_numbers)):
    print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}') 