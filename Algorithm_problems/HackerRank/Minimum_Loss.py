#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(prices):
    # Write your code here
    prev = prices[0]
    candidate = []
    for price in prices[1:]:
        if price[0]>prev[0]:
            candidate.append(prev[1]-price[1])
        prev = price
    return min(candidate)

if __name__ == '__main__':
    n = int(input().strip())
    prices = sorted(enumerate(map(int, input().rstrip().split())), key=lambda x: -x[1])
    result = minimumLoss(prices)
    print(result)