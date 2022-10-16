
basic_list = [1,2,3]
additional_list = [[1,2,3,4], [5,6,7,8], [9,10,11]]
basic_tuple = (1,2,3)
basic_set = {1,2,3}
basic_dict = {1: "one", 2:"two", 3:"three"}
basic_string = "One two three"
basic_num = 3

#Nested list
for nested_lists in additional_list:
    print(nested_lists)
    for values in nested_lists:
        print(values)

# while True:
#     variable = input("What is Your variable?: ")
#     match variable:
#         case "basic_list":
#             for i in basic_list:
#                 print(i)
#                 continue
#         case "basic_tuple":
#             for i in basic_tuple:
#                 print(i)
#         case "basic_set":
#             for i in basic_set:
#                 print(i)
#         case "basic_dict":
#             for i in basic_dict:
#                 print(i)
#         case "basic_string":
#             for i in basic_string:
#                 print(i)
#         case "basic_num":
#             print(f'"basic_num" cannot be entered, use range(basic_num) instead!')0
#             for i in range(basic_num):
#                 print(i)