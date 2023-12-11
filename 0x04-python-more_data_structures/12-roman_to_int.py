#!/usr/bin/python3

def roman_to_int(roman_string):
    
    if not isinstance(roman_string, (str)):
        return 0

    if roman_string == None:
        return 0

    r = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    ans = 0
    current = 0
    nxt = 0

    if len(roman_string) < 2:
        return r[roman_string]

    for val in range(len(roman_string)-1):
        current = r[roman_string[val]]
        nxt = r[roman_string[val+1]]

        if current < nxt:
            ans = ans - current
        elif current == nxt:
            ans = ans + current
        else:
            ans = ans + current
    ans = ans + r[roman_string[-1]]
    return ans
