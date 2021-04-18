import sys
from collections import deque
import time

sys.stdin = open("input.txt","r")

def Go_travel(guild):

    guild.sort()

    answer = 0
    count = 0

    for fear in guild:

        count += 1

        ###현재 인원이 어떤 사람의 공포도와 같거가 크다면 출발
        if count >= fear:
            
            answer += 1
            ###인원 초기화
            count = 0
    
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    people_list = list(map(int,sys.stdin.readline().split()))

    print(Go_travel(people_list))