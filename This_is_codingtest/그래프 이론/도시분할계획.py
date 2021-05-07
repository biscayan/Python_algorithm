import sys

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b: 
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    parent = [0] * (N+1)

    for i in range(1, N+1):
        parent[i] = i

    edges = []

    total_cost, max_cost = 0, 0

    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        edges.append((C,A,B))

    ### cost를 기준으로 오름차순 정렬
    edges.sort()
    
    for edge in edges:

        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            max_cost = cost

    ### max code를 제거함으로써 마을을 2개로 나눔
    result = total_cost - max_cost

    print(result)