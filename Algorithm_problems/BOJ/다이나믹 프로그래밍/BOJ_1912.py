import sys

sys.stdin = open("input.txt", "r")

def seq_sum(n):

    dp_table = [-1e9] * n
    dp_table[0] = num_list[0]

    answer = dp_table[0]

    for i in range(1, n):
        dp_table[i] = max(num_list[i], dp_table[i-1]+num_list[i])
        answer = max(answer, dp_table[i])
    
    return answer


if __name__ == '__main__':

    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))

    print(seq_sum(n))