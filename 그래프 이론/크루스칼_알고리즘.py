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

    ### vertex, edge
    v, e = map(int, input().split())

    parent_table = [0] * (v+1)

    edges = []
    result = 0

    for i in range(1, v+1):
        parent_table[i] = i

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost,a,b))

    edges.sort()

    for edge in edges:

        cost, a, b = edge

        ### 사이클이 발생하지 않을 때 집합에 포함
        if find_parent(parent_table, a) != find_parent(parent_table, b):
            union_parent(parent_table, a, b)
            result += cost

    print(result)