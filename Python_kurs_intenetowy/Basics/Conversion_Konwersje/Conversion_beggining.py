#float, int, str

from ast import Str


floatNum = 23.45454545
intNum = int(floatNum) # konwersja

print(type(intNum))
print(intNum)
print(int("2387423    ")) # spacje zostały zignorowane

tekst = "123.1232313"
float2 = float(tekst)
print()
print(float2)

print("Wartość float1: " + str(intNum))