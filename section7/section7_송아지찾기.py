import sys
from collections import deque

sys.stdin = open("input.txt","r")

def find_calf(location):

    queue = deque()

    queue.append(location)

    visited[location] = True

    while queue:

        ### 현재 현수의 위치
        cur_location = queue.popleft()

        if cur_location == E:
            break
        
        ### 현수는 +1, -1, +5 중 하나의 형태로 이동
        for next_location in [cur_location+1, cur_location-1, cur_location+5]:
            
            ### 좌표의 범위는 1~10000
            if next_location>=1 and next_location<=10000:
                
                ### 다음이동위치가 방문하지 않았던 곳일 때,
                if visited[next_location] == False:

                    queue.append(next_location)

                    visited[next_location] = True
                    count[next_location] = count[cur_location]+1

    print(count[cur_location])


if __name__ == '__main__':

    S, E = list(map(int, sys.stdin.readline().split()))
    
    ### 위치 방문여부를 체크
    visited = [False] * 10001

    ### 송아지가 있는 위치까지 가는 횟수를 저장
    count = [0] * 10001

    find_calf(S)