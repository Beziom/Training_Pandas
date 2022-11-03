"TRY = Avoiding errors - first one is only printed if error"
#try:
#except:
#finally:

try:
    print("try")
except ZeroDivisionError:
    print("You cannot divide by zero") #written only with ZeroDivisionError
except NameError:
    print("Name doesn't exist") #Written only when Name Error (will be not executed)
else:
    print("Else statement True") #Will be execuded when try will work (both with it)
finally:
    print("Finally") # It will be always issued (even with else or error)

"Raising exceptions ourselves"
#isinstance
#raise TypeError

var_must_be_string = "String"
if isinstance(var_must_be_string,str):
    print(var_must_be_string)
else:
    raise TypeError("Must be a string")

"Assert - stronger if statement"
a = 5
assert a == 5

"Excersise"
#Create a list
#Try to raise inec erroe
#alsoe add else and finally

list_1=[1,2,3,4]

try:
    print(list_1[4])
except IndexError:
    print("List conatins too much values")
else:
    print("Rucham Ci starą")
finally:
    print("Stara jest ruchana")