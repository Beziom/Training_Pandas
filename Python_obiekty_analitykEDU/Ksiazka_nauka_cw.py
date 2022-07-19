
from turtle import title


class Book(object):
    """Wirtualny szkic książki"""
    
    def __init__(self, title, author, date, owner):
        self.title = title
        self.author = author
        self.date = date
        self.owner = owner

    def information(self):
        informations = [self.title, self.author, self.date, self.owner]
        for i in informations:
            if i == self.author:
                print("~", self.author)
            else:
                print(i)
            
    
    def owner_change(self, new_owner):
        self.owner = new_owner

# Ćwiczenie 1: Należy utworzyć klasę książka. Klasa, powinna:
# Przechować informacje na temat: tytułu, ilości stron, autora, data wydania, właściciel
# Posiadać 2 metody / funkcje – 1 – zwraca informacje na temat książki, 2 – zmianę właściciela książki

book1 = Book("Nic - czyli jak nic nie robić", "Maciej", "19.06.2022", "Maciej Siewierski")
print()
book1.information()
book1.owner_change("Kamil")
print()
book1.information()

# Ćwiczenie 2: korzystając z wyżej zdefiniowanej klasy, utworzyć kilka obiektów klasy książka, po czym dodać je do listy książek. Lista książek, to zwykła zmienna typu 'lista’.

k1 = Book("Nic - czyli jak nic nie robić", "Maciej", "19.06.2022", "Maciej Siewierski")
k2 = Book("Tolkien", "Tolkien człowiek", "1945", "Maciuś")
k3 = Book("Badacz", "Człowiek niezdbadany", "1912", "Maciuś")

Book_list = [k1,k2]
Book_list.append(k3)
for i in Book_list:
    print(i.title)
