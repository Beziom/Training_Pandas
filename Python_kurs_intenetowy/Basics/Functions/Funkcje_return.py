#return nie jest obowiązkowe jeśli nie zwracamy wartości
def addNumbers(a,b,c):
    return a+b+c

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista") 
        return None # Jeśli lista jest pusta to zostanie zwrócone NONE
    result = 0

    for v in listData:
        result += v

    return result

print(sumListElements([]))

print(sumListElements([1,2,3,4,5,6]))

def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)

printList([])