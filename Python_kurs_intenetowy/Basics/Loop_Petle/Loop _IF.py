# Jeśłi rezultat będzie True to wykona działania

#if, elif, else

num = 5

if num >= 3:
    print(num, "większe lub równe 3")

if num == 5:
    print(num, "= 5")# 5 = 5

if num == 1:
    print(num, "= 1")# nic
elif num ==2:
    print(num, "= 2")# nic 
elif num ==5:
    print(num, "= 5")# 5 = 5


if 5 > 1: print("5 > 1")

if 10>2:
    print("10 > 2")
    if 4>1:
        print("4 > 1")
        if 3>2:
            print("3 > 2")

#if regards to boolean type

flag = True

if flag == True:
    print("flag = True")
if flag is True:
    print("flag is True")
if flag:
    print("flag is True")

flag = False

if flag != True:
    print("flag = True")
if flag is not True:
    print("flag is True")
if not flag:
    print("flag is True")