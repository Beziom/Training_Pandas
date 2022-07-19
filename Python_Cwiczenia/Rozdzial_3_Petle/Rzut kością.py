# Gra w rzut kością

import random

#generowanie liczb od 1 do 6

kosc1 = random.randint(1,6)
input(kosc1)
kosc2 = random.randrange(6) + 1
input(kosc2)
total = kosc1 + kosc2

print("Wyrzuciłeś", kosc1, "jako pierwszy rzut, oraz", kosc2, "jako drugi rzut, suma kości to", total)

input("Zakończ enterkiem")
