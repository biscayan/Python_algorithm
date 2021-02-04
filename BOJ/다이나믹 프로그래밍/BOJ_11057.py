import sys

sys.stdin = open("input.txt", "r")

def Ascending_num(n):

    dp_table = [[0] * 10 for _ in range(n+1)]

    ### Base(n이 1일 때)
    for col in range(10):
        dp_table[1][col] = 1

    for i in range(2,n+1):
        for j in range(10):
            for k in range(j+1):
                dp_table[i][j] += dp_table[i-1][k]

    result = sum(dp_table[n]) % 10007

    print(result)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    Ascending_num(N)