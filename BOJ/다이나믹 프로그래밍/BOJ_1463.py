import sys

sys.stdin = open("input.txt", "r")

def make_one(x):

    dp_table = [0] * (x+1)

    if x == 1:
        return 0

    for i in range(2,x+1):
        
        dp_table[i] = dp_table[i-1] + 1

        if i%2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i//2]+1)

        if i%3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i//3]+1)

    return dp_table[x]


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    print(make_one(N))