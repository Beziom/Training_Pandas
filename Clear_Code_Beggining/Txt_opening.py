"Opening a folder manually"
# file = open('Clear_Code_Beggining/test.txt')
# print(list(file))
# file.close()

"Open and close automatically"
# with open('Clear_Code_Beggining/test.txt') as file:
#     print(file.read()) #All file as a string 
#     for line in list(file):
#         print(line)

"Write a file"
# with open('Clear_Code_Beggining/test.txt', 'w') as file: # a as append, w as write, r as read 
#     file.write("\nXXXXWrite some more textXXXX")

# create a new text_file and draw a tree in it

"Excersise"
#Create a new test fle and fraw a tree in it
with open("Clear_Code_Beggining/tree.txt",'w') as file:
    tree_string = """        X 
       XXX
      XXXXX
     XXXXXXX
    XXXXXXXXX
        X
        X"""
    file.write(tree_string)

