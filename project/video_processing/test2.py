import matplotlib.pyplot as plt
import numpy as np


original_list = [[1,5], [2, 4], [3, 3], [4, 2], [5, 1]]

def reverse_y_elements_tuple(original_list):
    print(original_list)
    new_list = []
    x = []
    y = []  
    for a,b in original_list:
        print(a, b)
        x.append(a)
        y.append(b)
    y.reverse()
    print(x)
    print(y)
    new_list = zip(x, y)
    print(new_list)

def reverse_y_elements_list(original_list):
    print(original_list)
    # new_list= []
    x = []
    y = []  
    for a,b in original_list:
        print(a, b)
        x.append(a)
        y.append(b)
    y.reverse()
    print(x)
    print(y)
    new_list = list(map(list, zip(x, y)))
    # map(new_list, zip(x, y))
    print(new_list)

reverse_y_elements_tuple(original_list)
reverse_y_elements_list(original_list)

# new_list = []
# new_sub_list = []
# for sub_list in original_list:
#     for element in sub_list:
#         print("{}".format(element))
#         # i = i+1
#         # j = j-1
#         # new_sub_list[i][] = sub_list