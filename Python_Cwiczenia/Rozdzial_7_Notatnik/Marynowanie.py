#Marynowanie plików (kompresowanie)
#int, str, tuple, list, dict
#pickle, przechowywanie w pliku bardziej złożonych danyh
#pickle.dump()
#shelve, magazynowanie zamarynowanych obiektów

import pickle, shelve

#utworzenie list do marynowania
print("Marynowanie list.")
look = ["przystojny", "ładny", "śliczny"]
features = ["nerwowy", "empatyczny", "fajny"]
like = ["konsola", "śpiew", "taniec"]

#otwarcie nowego pliku w kodzie binarcnym "wb"
f = open("pikiel.dat", "wb")

#marynowanie i magazynowanie trzech list pickle.dump()
pickle.dump(look, f)
pickle.dump(features, f)
pickle.dump(like, f)
f.close()

#odmarynowywanie pickle.load()
print("Odmarynowanie list.")
f = open("pikiel.dat", "rb")
look = pickle.load(f)
features = pickle.load(f)
like = pickle.load(f)

print(look)
print(features)
print(like)

#shelve przechowuje obiekty a nie znaki (słownik)
print("Odkładanie list na półkę")
s = shelve.open("pikle2.dat") # otwarcie półki

s["look"] = look #Klucz look tworzy parę z zawartością (listą) file
s["features"] = features
s["like"] = like

s.sync() # dane zostały zapisane

#pobranie danych z półki
print("Pobieanie list z pliku półki: ")
print("look", s["look"])
print("features", s["features"])
print("like", s["like"])