#Gra w karty
# Demonstruhe tworzenie kombinacji obiektów

#Objects
class Card(object):
    """Karty do gry"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "8", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"] # c - trefle, d - kara, h - kierym s - piku

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self): #Łańcuch znaku repzrezentujący całą rękę
        rep = self.rank + "" + self.suit
        return rep

class Hand(object):
    """Ręka - karty fo gry w ręku gracza"""
    def __init__(self):
        self.cards = [] # Każy pojedynczy obiekt będzie miał atrybut cards który jest listą

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self): # kadowanie isty kart poprzez przypisanie pustej listy
        self.cards = []

    def add(self, card): # dodanie obiektu do atrybutu cards  
        self.cards.append(card)
    
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

#część główna

card1 = Card("A","c")
print()
print("Wyświetlenie obiektkarty (klasy Card):")
print(card1)            

print()
card2 = Card("2", "c")
card3 = Card("3", "c")
card4 = Card("4", "c")
card5 = Card("5", "c")

print()
print("Wyświetlanie reszy obiektów po jednym na raz:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("Wyświetlam zawartość mojej ręki przed dodaniem jakichkowiek kart:")
print(my_hand)

my_hand.add(card1) # 2c
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)

print("Wyświetlenie zawartości ręki po dodaniu 5 kart:")
print(my_hand) # Ac 2c 3c 4c 5c

your_hannd = Hand()
my_hand.give(card1, your_hannd)
my_hand.give(card2, your_hannd)
print("Przekazanie kart do innej ręki")
print(your_hannd)
print(my_hand)

my_hand.clear()
print(my_hand)