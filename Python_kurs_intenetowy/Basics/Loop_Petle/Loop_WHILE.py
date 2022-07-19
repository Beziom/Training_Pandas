#Działa tak długo jak warunek zwraca True
#Działa z else!

number = 5

while number > 0:
    print(number)
    number -= 1

number = 1

while number < 6:
    print(number)
    number += 1

#Dodawanie cyfr
num = 5
while True:
    print("Wprowadź liczbę lub exit aby zakończyć")
    strData = input()
    if strData == "exit": break # Jeśli będzie exit to break
    num += int(strData)
    print("wartość po dodaniu liczby: " + str(num))

number = 3
while number > 0:
    print(number)
    number -= 1
else:
    print("number po pętli: " + str(number))