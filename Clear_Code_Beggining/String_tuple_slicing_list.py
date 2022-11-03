excersise_string = "I like Puppies"
print(excersise_string.replace("Puppies", "Kitties"))
print(excersise_string.replace("Puppies"\
,"Kitties"))

"Deklarowanie zmiennych"
a,b=[1,2]
print(a,b)
weapon,health,mana = "+15dmg", 150, 15
print(f'{weapon} {health} {mana}')

"Reverse slicing"
data = [1,2,3,4,5,6]
print("Reverse slicing", data[::-1])

"Turning a strin into list (strip and slip)"
text="This is a simple list with split function"
print(text.split()) # ['This', 'is', 'a', 'simple', 'list', 'with', 'split', 'function']
print(text.split("t")) # ['This is a simple lis', ' wi', 'h spli', ' func', 'ion']
print(list(text)) # ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'i', 'm', 'p', 'l', 'e', ' ', 'l', 'i', 's', 't', ' ', 'w', 'i', 't', 'h', ' ', 's', 'p', 'l', 'i', 't', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n']
print('Gap'.join(["one", "two"])) #oneGaptwo
excersise = str(data).strip("[").strip("]").replace(",", ""); print(excersise)