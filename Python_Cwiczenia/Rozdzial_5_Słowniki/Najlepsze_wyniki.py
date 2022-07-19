#Wyświetlanie wynikó

from re import S

#dane
scores = []
choice = None

#Pętla
while choice != 0:
    print("""\nNajlepsze wyniki \n0 - zakończ \n1 - pokaż wyniki \n2 - dodaj wynik \n3 - usuń wynik \n4 - posortuj""")
    choice = input("Wybierasz: ")

    #Włączenie programu
    if choice == "0":
        print("\nProgram zakończony, dziękuję za korzystanie")
        break
    
    #Wyświetlenie wyników
    elif choice == "1":
        print("\nNajlepsze wyniki")
        for i in scores:
            print(i)
    
    #Dodawanie wyników
    elif choice =="2":
        print("\nDodawanie wyniku")
        score = int(input("Jaki wynik chcesz dodać?"))
        scores.append(score)
        print("Dodano wynik", score)

    # #Dusuwanie wyników
    elif choice == "3":
        print("\nUsuwanie wyniku")
        score = int(input("Któy wynik chcesz usunąć?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Wybrano nieprawidłową wartość")

    elif choice == "4":
        scores.sort(reverse=True)

input("Wciśnij Enter aby zakończyć program")