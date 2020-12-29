import sys

sys.stdin = open("input.txt", "r")

def cut_tree(trees, middle):
    
    tree_len = 0

    for tree in trees:

        cutted = tree - middle

        ###잘려진 부분이 0이나 음수이면 추가x
        if cutted > 0:
            tree_len += cutted
    
    return tree_len


if __name__ == "__main__":

    N, M = map(int, sys.stdin.readline().split())
    tree_list = list(map(int, sys.stdin.readline().split()))

    ###index 초기화
    l_idx = 0
    r_idx = max(tree_list)

    answer = 0

    while l_idx <= r_idx:

        m_idx = (l_idx + r_idx)//2

        ###정답을 찾을 때까지 범위를 좁혀나감
        if cut_tree(tree_list, m_idx) >= M:
            answer = m_idx
            l_idx = m_idx + 1
        
        else:
            r_idx = m_idx - 1

    print(answer)