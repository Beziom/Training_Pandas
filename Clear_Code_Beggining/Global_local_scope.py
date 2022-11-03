from audioop import mul


a = 10

# def test_func():
#     capacity = 2
#     print(capacity)

# def test_func_2():
#     capacity = 200
#     print(capacity)

# test_func()
# test_func_2()

def test_func_3(a):
    # global a - is a optional but not recomended
    a+=2
    return a

print(test_func_3(a))
a = test_func_3(a)

#Excersise
multiplier = 15
has_calculated = False

def multiply_calculatro(number):
    global has_calculated
    has_calculated = True
    result = number * multiplier
    return result

print(multiply_calculatro(15))
    


