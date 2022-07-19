#break
data = [1,2,3,4,5]
for i in data:
    if i ==3:
        break #PO 3 ITERACJI NASTĘPUJE KONIEC KODU
    print(i*2)


print("")

#continue
for i in data:
    if i == 3 or i ==5:
        continue
    print(i) # 1,2,4

#pass
if 10 > 2:
    pass # nie ma błędu ponieważ jest pass (pozwala na zrobienie błędu)



