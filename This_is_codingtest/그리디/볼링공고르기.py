import sys

sys.stdin = open("input.txt","r")

def choose_ball(ball_list):

    count = 0

    for i in range(N):
        for j in range(i+1,N):
            if ball_list[i] != ball_list[j]:
                count += 1
    
    return count

if __name__=='__main__':
    
    N, M = map(int,sys.stdin.readline().split())

    ball_list = list(map(int,sys.stdin.readline().split()))

    print(choose_ball(ball_list))