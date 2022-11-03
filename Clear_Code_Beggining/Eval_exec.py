"Eval"
print(eval('"Test".upper()'))
print(eval("5+5"))

dupa = True if eval("5+5") == 10 else False
print(dupa)

"Exec"
exec("a = 5")
print(a)

"Excersise"
my_string = "test"
print(my_string.upper())
print(my_string.lower())
print(my_string.title())
print(my_string.casefold())

for operations in ["upper", "lower", "title", "casefold"]:
    print(eval(f"my_string.{operations}()"))
