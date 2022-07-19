#lambda pozwala na utworzenie anonimowych funkcji
#lambda przydatna jest dla funkcji wyższego rzędu gdzie argument przyjmuje inne funkcje lub zwracają funkcje

#map(func, seq) przyjmują funkcję która wywoła na wszystkich elementach seq (sekwencji) i zwóci cekwencję zmodyfikowanych przez func elementów w postaci iteratora (użyteczne w listach)
#map(lambda, lista)
#filter() pozwala na filrowanie sekwencji , zwraca tylko te elementy która dla wyrażenia lambda zwróci True (na każdym z elementów)
#reduce() musi być zaimporowana (from functools import reduce) - reduce redukuje wszystkie wartości do pojedyńczej wartości

from functools import reduce
sum = lambda a,b: a + b #a,b - parametry

print(sum(4,5)) # 9
print(sum(14,5)) # 19

def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2) # jest przechowana wartość 2, wartością wpisywaną jest 2
print(doubler(4)) # 8

listData = [0,1,2,3]

result = list(map(lambda a: a*3, listData)) # Zawartość listy zostaje pomnożona o 10

print(result)

result = list(filter(lambda a: a>1, listData)) # szukamy wartości z listy które są większe od 1
print(result) # [2,3]

result = reduce(lambda x,y: x+" "+y, ("Ola", "Ania", "xD", "LOL")) # redukcja do pojedyńczej wartości liczbowej

print(result)#OlaAnia