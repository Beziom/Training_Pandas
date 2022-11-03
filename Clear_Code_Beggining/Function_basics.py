def test_function(): #Creating a function
    print("Hello")
    test = 1+2
    print(test)

def better_calculator(num1, num2, operation):
    if operation == "plus" or operation == "+": result = num1 + num2; print(f'{num1} + {num2} = {result}')
    elif operation == "minus" or operation == "-": result = num1 - num2; print(f'{num1} - {num2} = {result}')
    elif operation == "divide" or operation == "/": result = num1 / num2; print(f'{num1} / {num2} = {result}')
    elif operation == "times" or operation == "*": result = num1 * num2; print(f'{num1} * {num2} = {result}')
    elif operation == "power of" or operation == "**": result = num1 ** num2; print(f'{num1} ** {num2} = {result}')
def calculator_add(num1, num2):
    result = num1 + num2
    print(result)

test_function() # calling a function
calculator_add(2,3)

better_calculator(5,10,"**")