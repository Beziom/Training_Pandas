#Krajacz pizzy

word = "pizza" 

print("""'Ściągawka' tworzenia wycinków
 0   1   2   3   4   5
 +---+---+---+---+---+
 | p | i | z | z | a |
 +---+---+---+---+---+
-5  -4  -3  -2  -1
""")

print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monit 'Początek:'\n"
+ "naciśnij klawisz Enter.")

start = None #Wartość traktowana jako False (strażnik do While)

while start != "":
    start = (input("\nPoczątek: "))

    if start:
        start = int(start)

        finish = int(input("Koniec "))

        print("word[", start, ":", finish, "] to", end = " ")
        print(word[start:finish]) # printowanie indeksów

input("Zakończe Enterkiem")
