#Dziedziczenie klasy
# Gra w karty 2.0

class Card(object):
    """Karty do Gry"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + "" + self.suit
        return rep
    
class Hand(object):
    """Ręka gracza"""

    def __init__(self):
        self.cards = [] # Pusta lista cards

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "/t"
        else:
            rep = "<puste>"
        return rep
    
    def clear(self):
        self.cads = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.card.remove(card)
        other_hand.add(card)

class Deck(Hand): 
    """Talia do kart w gry"""
    #Klasa jest oparna na nagłówku HAND
    #  __init__(),
    #  __str__(),
    #  clear(),
    #  add(),
    #  give().
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.Ranks:
                self.add(Card(rank, suit))

 