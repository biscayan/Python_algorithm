import sys

sys.stdin = open("input.txt", "r")

def deploy_soldier(array):

    dp_table = [1] * (N)

    ### LIS algorithm
    for i in range(1,N):
        for j in range(i):
            if array[i] > array[j]:
                dp_table[i] = max(dp_table[j]+1, dp_table[i])
    
    result = N - max(dp_table)

    return result


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = list(map(int, sys.stdin.readline().split()))
    array.reverse()

    print(deploy_soldier(array))