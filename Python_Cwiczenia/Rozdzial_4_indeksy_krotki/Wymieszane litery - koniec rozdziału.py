# Wymieszane litery

import random

#utworzenie sekwencji
words = ("pyhon", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#wybierz losowo jedno słowo z sekwencji
word = random.choice(words)

#utworzenie zmiennej do sprawdzenie czy odpowiedź jest poprawna
correct = word

input("\nZakończ program Enterkien.")

#utworzenie 'pomieszanego' słowa
jumble = "" # wartownik
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
""")

print("Zgadnij jakie to słwo:", jumble)
guess = input("\nTwoja odpowiedź: ")

while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    
if guess == correct:
    print("Zgadza się! Zgadłeś!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")                                  



