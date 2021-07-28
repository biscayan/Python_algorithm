import sys
import re
from itertools import combinations

sys.stdin = open("input.txt", "r")

def teaching(words):

    answer = 0
    
    # can't teach all words
    if K < 5:
        return 0

    # can teach all words
    if len(not_antic) <= K-5:
        return N

    comb_list = list(combinations(not_antic, K-5))

    for comb in comb_list:
        count = 0
        total = antic.union(comb)
        for word in words:
            if word.issubset(total):
                count += 1
        answer = max(answer, count)

    return answer

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    antic = set('antic') #anta tica
    not_antic = set()
    words = []
    for _ in range(N):
        word = set(map(str, sys.stdin.readline().strip()))
        words.append(word)
        # add not_antic alphabets
        not_antic.update(word-antic)
    print(teaching(words))