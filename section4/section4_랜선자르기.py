import sys

sys.stdin = open("input.txt", "r")

def count_lan(line_len,lines):
    cnt = 0
    for i in range(len(lines)):
        cnt += lines[i]//line_len
    return cnt


if __name__=='__main__':

    K, N = map(int, input().split())

    line_list = []
    max_len = 0

    for _ in range(K):
        lan = int(input())
        line_list.append(lan)

    ###잘라진 랜선이 가질 수 있는 길이의 범위 1 ~ 802
    l_idx = 1
    r_idx = max(line_list)

    while l_idx <= r_idx:

        m_idx = (l_idx + r_idx)//2

        if count_lan(m_idx, line_list) >= N:
            max_len = m_idx
            ###현재 범위에서 오른쪽만 검색
            l_idx = m_idx+1
        
        else:
            ###현재 범위에서 왼쪽만 검색
            r_idx = m_idx -1

    print(max_len)
