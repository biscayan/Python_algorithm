import sys

N, M = map(int, sys.stdin.readline().split())
A, B = list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))

result = []
idx1, idx2 = 0, 0

while idx1<N and idx2<M:
    if A[idx1] < B[idx2]:
        result.append(A[idx1])
        idx1 += 1
    else:
        result.append(B[idx2])
        idx2 += 1

result.extend(x for x in A[idx1:]), result.extend(x for x in B[idx2:])
print(*result)