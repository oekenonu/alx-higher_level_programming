#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    ans = 0
    divisor = 0
    for i in my_list:
        ans += (i[0] * i[1])
        divisor += i[1]

    return (ans/divisor)
