import sys
from itertools import combinations

def lotto(k, array):
    sub_arraies = list(combinations(array, k))
    for sub_array in sub_arraies:
        S = list(combinations(sub_array, 6))
        for seq in S:
            print(*seq)

if __name__ == '__main__':
    while True:
        sequence = list(map(int, sys.stdin.readline().split()))
        if sequence[0] == 0:
            break
        k, array = sequence[0], sequence[1:]
        lotto(k, array)
        print()