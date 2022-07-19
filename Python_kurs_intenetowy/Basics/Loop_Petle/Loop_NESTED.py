# Nested Loops
# break, continue, pass - nic nie robi, tam gdzie wymagane dodanie jakiegokolwiek kodu, nie będzie błędu (nieskończony projekt)

listsData=[
    [0,1,2,3,4],
    ["Ola", "Ala", "Adam"],
    [10,"Adam", 20, "Ania"]
]

for listData in listsData:
    print(listData) #Wyświetlenie 3 list
    for v in listData: #Wyświetlenie zawartości 3 list
        print(v)


  