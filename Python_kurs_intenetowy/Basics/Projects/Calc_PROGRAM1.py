#kalkulator

num = 0 # zmienna do przechowania wartości
operation = None 
reset = True # informacja że musimy zresetować kalkulator
result = None # przechowane wyniki działania
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True: # reset kalkulatora
        num = int(input("Podaj liczbę startową: "))
        reset = False

    operation = input("Podaj operację artmetyczną jak np." + str(calcOperations) + " lub exit jeśli koniec lub reset: ")

    if operation == "exit":
        print("Dziękujemy za skorzystanie z programu!")
        break # przerywamy pętle while True
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja")
        continue

    secondNum = int(input("Wprowadź drugą liczbę: "))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum
    
    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum
    
    print("Wynik operacji " + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result # zapamiętanie wartośi żeby uzyć do następnych obliczeń
    result = None


