#Tworzenie pętli nieskończonej i zastosowanie break oraz continue

print("Pętla nieskończona z funkcją break")
count = 0

while True: # pętla jest wykonywana bez końca = chyba że jest warunek wyjścia
    count = count + 1 #każda iteracja to +1
    if count > 10:
        break # przerwanie
    if count == 5: #pominięcie liczby 5
        continue # skocz z powrtoem do początku nowej interacji
    print(count)

input("Zakończ Enterkiem")
