#id() zwraca unikalny identyfikator dla każdego przekazanego obiektu
# int, float, bool, str, Tuple, frozenset = niemutowalne
# list, set, dict = mutowalne

a = 1
addr1 = id(a)
a += 1
addr2=id(a) # Inna wartość
print(addr1)
print(addr2)
print(addr1 ==  addr2) # False

listData = [0,1,2]
addr1 = id(listData)

listData += [3,4,5]
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2) #True

