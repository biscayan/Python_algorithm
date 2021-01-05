import sys

sys.stdin = open("input.txt", "r")

def swap_element(array_a, array_b):

    sorted_array_a = sorted(array_a)
    sorted_array_b = sorted(array_b, reverse = True)

    for i in range(K):
        ### a의 요소가 b의 요소가 작을 때만
        if sorted_array_a[i] < sorted_array_b[i]:
            ### swap
            sorted_array_a[i], sorted_array_b[i] = sorted_array_b[i], sorted_array_a[i]
        else:
            break

    result = sum(sorted_array_a)

    return result

if __name__ == '__main__':

    N, K = map(int, sys.stdin.readline().split())

    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    print(swap_element(A, B))