### 경로 압축을 적용하여 개선
def find_parent(parent, x):
    
    ### 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
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

    ### vertex, edge
    v, e = map(int, input().split())

    parent_table = [0] * (v+1)

    ### 부모를 자기 자신의 값으로 초기화
    for i in range(1,v+1):
        parent_table[i] = i

    ### union연산 수행
    for i in range(e):
        A, B = map(int, input().split())
        union_parent(parent_table, A, B)

    print("각 원소가 속한 집합 : ", end=' ')
    for i in range(1, v+1):
        print(find_parent(parent_table, i), end=' ')

    print()

    print("부모 테이블 : ", end=' ')
    for i in range(1,v+1):
        print(parent_table[i], end=' ')