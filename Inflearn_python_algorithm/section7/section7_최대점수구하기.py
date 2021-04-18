import sys

sys.stdin = open("input.txt","r")

def max_score(lvl, score_sum, time_sum):

    global result

    if time_sum > M:
        return 
        
    if lvl == N:
        if score_sum > result:
            result = score_sum
        
    else:
        max_score(lvl+1, score_sum+array[lvl][0], time_sum+array[lvl][1])
        max_score(lvl+1, score_sum, time_sum)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    array = []
    
    for _ in range(N):
        score, time = map(int, sys.stdin.readline().split())
        array.append((score,time))

    result = 0

    max_score(0, 0, 0)

    print(result)