from xmlrpc.client import boolean


def test(a:int = 5,b:int = 10) -> int: # a and b are interers and output -> we want to be integer
    """
    Simple function which print out 2 arguments

    Args:
        a (int): First argument to print
        b (int): Second argument to print
    """
    print(a)
    print(b)
test()
print(test.__doc__)
help(test) # checking