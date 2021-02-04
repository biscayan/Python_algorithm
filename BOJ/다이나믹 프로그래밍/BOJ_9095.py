import sys

sys.stdin = open("input.txt", "r")

def one_two_three(n):

    dp_table = [0] * 11

    dp_table[1], dp_table[2], dp_table[3] = 1, 2, 4

    if n >= 4:
        for i in range(4, n+1):
            dp_table[i] = dp_table[i-3] + dp_table[i-2] + dp_table[i-1]

    result = dp_table[n]

    print(result)

if __name__ == '__main__':

    ### test case
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        one_two_three(N)