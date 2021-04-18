import sys

sys.stdin = open("input.txt","r")

def Bag_problem(w,v):

    for i in range(w, limit+1):
        dp_table[i] = max(dp_table[i-w]+v, dp_table[i])

if __name__ == '__main__':

    n, limit = map(int, sys.stdin.readline().split())

    dp_table = [0] * (limit+1)

    for _ in range(n):
        weight, value = map(int, sys.stdin.readline().split())
        Bag_problem(weight, value)

    result = max(dp_table)

    print(result)