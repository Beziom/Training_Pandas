#Program receiving inpupt for number of rows and draw Christmas Tree
branches = "X"
number_of_branches = int(input("How many branches should have\
the Christmass Tree?"))
print()
for i in range(number_of_branches):
    if i <= (number_of_branches-5):
            print(branches.center(2*number_of_branches," "))
            branches += "XX"
    elif i > (number_of_branches - 3): print("X".center(2*number_of_branches," "))
print()