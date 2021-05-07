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

    for i in range(N+1):
        parent[i] = i

    for _ in range(M):
        oper, a, b = map(int, sys.stdin.readline().split())

        ### 팁 합치기
        if oper == 0:
            union_parent(parent, a, b)

        ### 같은 팀 여부 확인
        elif oper == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")