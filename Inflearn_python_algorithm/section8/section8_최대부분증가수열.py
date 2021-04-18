import sys

sys.stdin = open("input.txt", "r")

def Increaing_seq(max_num):

    dp_table = [0] * (max_num+1)

    dp_table[num_seq[0]] = 1

    for i in range(1, N):
        for j in range(i):
            if num_seq[i] > num_seq[j]:
                dp_table[num_seq[i]] = max(dp_table[num_seq[i]], dp_table[num_seq[j]]+1)
            else:
                dp_table[num_seq[i]] = max(dp_table[num_seq[i]], 1)

    result = max(dp_table)
    
    print(result)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    num_seq = list(map(int, sys.stdin.readline().split()))

    max_num = max(num_seq)

    Increaing_seq(max_num)