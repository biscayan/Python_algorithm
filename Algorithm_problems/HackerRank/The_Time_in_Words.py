#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    dict = {
        1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter',
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
        30:'half'}

    if m == 0:
        answer = f"{dict[h]} o' clock"
    elif m == 1:
        answer = f"{dict[m]} minute past {dict[h]}"
    elif m>1 and m<=20:
        if m == 15:
            answer = f"{dict[m]} past {dict[h]}"
        else:
            answer = f"{dict[m]} minutes past {dict[h]}"
    elif m>=21 and m<=29:
        answer = f"{dict[20]} {dict[m-20]} minutes past {dict[h]}"
    elif m == 30:
        answer = f"{dict[m]} past {dict[h]}"
    elif m>30 and m<40:
        answer = f"{dict[20]} {dict[60-m-20]} minutes to {dict[h+1]}"
    elif m>=40:
        if m == 45:
            answer = f"{dict[60-m]} to {dict[h+1]}"
        else:
            answer = f"{dict[60-m]} minutes to {dict[h+1]}"
    return answer

if __name__ == '__main__':
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)