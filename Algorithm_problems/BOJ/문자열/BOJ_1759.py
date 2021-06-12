import itertools
import sys

sys.stdin = open("input.txt", "r")

def make_pwd(n):

    vowels = ['a','e','i','o','u']

    for pwd in itertools.combinations(alphabets, n):

        vowel_cnt, consonant_cnt = 0, 0

        for p in pwd:
            if p in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(pwd))

if __name__ == '__main__':
    L, C = map(int, sys.stdin.readline().split())
    alphabets = list(sys.stdin.readline().split())

    alphabets.sort()

    make_pwd(L)