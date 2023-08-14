#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    greater = my_list[0]
    for i in my_list:
        if i > greater:
            greater = i
    return greater
