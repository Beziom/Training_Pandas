# def test_function(arg1,arg2,arg3,arg4):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     print(arg4)

# test_function(
#     arg1 = 1,
#     arg2 = "hello",
#     arg4= "yoloooo",
#     arg3= "mimimimi")

# def test_function_test(arg1,arg2,arg3,arg4 = "Dupa"): # if it is declared it is not needed to be appear in functions parameters
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     print(arg4)

# test_function_test(
#     arg1 = 1,
#     arg2 = "hello",
#     arg3= "yoloooo")

def greeter(person = "Person", greet = "Hello", weekday = "Monday"):
    print(f'{greet} {person}')
    print(f'It is {weekday}')

greeter()
