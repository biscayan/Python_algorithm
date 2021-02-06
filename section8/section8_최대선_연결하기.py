import sys

sys.stdin = open("input.txt", "r")

def Connect_line(n):

    dp_table = [0] * n

    dp_table[0] = 1

    for i in range(1,n):
        for j in range(i):
            if num_list[i] > num_list[j]:
                dp_table[i] = max(dp_table[i], dp_table[j]+1)
            else:
                dp_table[i] = max(dp_table[i], 1)

    print(max(dp_table))

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    num_list = list(map(int, sys.stdin.readline().split()))

    Connect_line(N)