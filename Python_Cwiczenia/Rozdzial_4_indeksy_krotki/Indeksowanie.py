# Indeksowanie
import random

word = input("Wprowadź swoją nazwę do analizy")

print("Wartość zmiennej to", word)

high = len(word)
low =-len(word)
position = 0
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t,", word[position])

input("Zakończ program Enterkiem")
