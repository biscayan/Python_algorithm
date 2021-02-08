import sys

sys.stdin = open("input.txt", "r")

def Max_Score(score,time):

    ### 중복을 방지하기 위해 뒤에서부터 진행
    for i in range(M, time-1, -1):
        dp_table[i] = max(dp_table[i], dp_table[i-time]+score)

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    dp_table = [0] * (M+1)

    for _ in range(N):

        s, t = map(int, sys.stdin.readline().split())
        
        Max_Score(s,t)

    print(dp_table[M])