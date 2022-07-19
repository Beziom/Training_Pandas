#Praca z krotkami

#Dodawanie krotek
tuple1 = (1,2,3,4) + (5,6,7,8) +tuple([9]) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tuple1))
print(tuple1)

#zwielokrotnienie
print((1,2) * 4) #(1, 2, 1, 2, 1, 2, 1, 2)

#Czy element jest w krotce
print(9 in tuple1) # True

#Element krotki
print(tuple1[1])# 3

#Długość
print(len(tuple1)) # 9 elementów

#mininalma i max wartośći

print(min(tuple1)) # 1
print(max(tuple1)) # 9