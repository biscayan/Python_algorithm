import sys

sys.stdin = open('input.txt','r')

def Count(mid):

    #첫번째 마구간은 기본적으로 말이 있다고 가정
    horse = 1 
    end_point = stable_list[0]

    for i in range(1,n):
        if stable_list[i] - end_point >= mid:
            horse += 1
            end_point = stable_list[i]
    
    return horse

if __name__=='__main__':

    n, c = map(int, sys.stdin.readline().split())

    stable_list = []

    for _ in range(n):
        stable = int(sys.stdin.readline())
        stable_list.append(stable)

    stable_list.sort()

    l_idx = 1
    r_idx = stable_list[-1]

    answer = 0

    while l_idx <= r_idx:

        m_idx = (l_idx + r_idx)//2

        if Count(m_idx) >= c:
            answer = m_idx
            l_idx = m_idx + 1

        else:
            r_idx = m_idx - 1

    print(answer)