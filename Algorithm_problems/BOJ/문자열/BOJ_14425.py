import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())

S = []
answer = 0

for _ in range(N):
    N_strings = sys.stdin.readline()
    S.append(N_strings)

for _ in range(M):
    M_strings = sys.stdin.readline()
    if M_strings in S:
        answer += 1
        
print(answer)