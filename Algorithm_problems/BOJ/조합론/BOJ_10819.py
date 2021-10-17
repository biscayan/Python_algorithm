from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
per_list = list(permutations(A))
answer = 0
for per in per_list:
    tmp = 0
    for i in range(0, N-1):
        tmp += abs(per[i]-per[i+1])
    answer = max(answer, tmp)
print(answer)