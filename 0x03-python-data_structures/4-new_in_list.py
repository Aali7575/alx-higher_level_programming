#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        print(my_list)
    if idx >= length:
        print(my_list)
    print(my_list)
    my_list[idx] = element
    print(my_list)
