import sys
sys.stdin = open("input.txt", "r")

def find_num(X, A):
    left, right = 0, N-1
    while left <= right:
        mid = (left+right) // 2
        if X < A[mid]:
            right = mid-1
        elif X > A[mid]:
            left = mid+1
        else:
            return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    N_list = list(map(int, sys.stdin.readline().split()))
    N_list.sort()
    M = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split()))
    for num in M_list:
        print(1) if find_num(num, N_list) else print(0)