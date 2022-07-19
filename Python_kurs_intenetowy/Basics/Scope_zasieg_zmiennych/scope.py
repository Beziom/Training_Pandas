
number = 12 # zmienna globalna

def test1():
    print(number) # 12

test1()

def test2():
    number = 100
    print(number) # 100

print()

test2() #100
print(number) #12 zmienna została stworzona w funkcji więc brana jest globalna
print()

print("TEST3 z pętlami w funkcji")
def test3():
    number = 100
    print(number) # 100
    if 1 == 1:
        print(number) # 100
        if 2 == 2:
            number = 50
            print(number) # 50
    print(number) # 50 (był utworzone w pętli if (zastąpił zmienną globalną wewnątrz funkcji))

test3()
print(number)
print() 

print("TEST 4 ze zmienną globalną")

def test4():
    global number
    number = 5 #zmieniona zostaje globalna wartość number
    print("test4", number) # 5
    if 1 == 1:
        number = 6
        print("test4", number) #6

test4()
print("Global number after test4", number) # 6 zmieniony global w pętli

print()
print("TEST5 z parametrem")
number = 10
def test5(number):
    print("Test 5 para: ", number)
    number = 20
    print("Test 5 after change: ", number) # 20

test5(33) # 33
print("number after test5(): ", number) # 10

print()
number = 10

def foo():
    print("foo() number:", number) # 10

def bar():
    number = 9
    print("bar() number", number) # 9
    foo()

print("FUNKCJI foo () zagnieżdżona funkcja")
bar()
print("Global number after foo() bar(): ", number)

print("\ncheck1 and check2")
number = 10
def check1():
    number = 12
    print("check1() number:", number) # 12
    def check2(): 
        print("check2() number", number) 
    check2()

check1()
print("Global number after check1():", number)

#if, while, try, except = utworzona zostaje zmienna globalna (jeśli pętla jest nieprawdziwa to nie jest utworzona)

