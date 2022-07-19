# Zastosowanie pętli if (sle i elif)

import random

rzut = random.randint(1,3)

if rzut == 1:
    print("""Nastrój
masz
wesoły
koleżko""")
elif rzut == 2:
    print("""Nastrój
masz
średni
koleżko""")
else:
     print("""Nastrój
masz
do
dupy""")

input("\n\nZakończ Enterkiem")
