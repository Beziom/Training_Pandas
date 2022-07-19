# Walka z potworem

print("Witaj poszukiwaczu przygód, napadł Cię troll, nieciekawa sprawa, ale spokojnie, poradzisz sobie,\n stawaj do WALKI!")
import random

health = 30
trolls = 0
damage = random.randint(1,3)

while health > 0:
    trolls += 1
    damage = random.randint(1,3)
    health -= damage
    print("Bohater pokonuje trolla, ale otrzymuje obrażenia wyskości", damage, "i zostaje mu", health, "punktów zdrowia")

print("Twój bohater walczył dzienie i zabił", trolls, "trolli")
input("\n\nZakończ enterkiem")
