from collections import deque

#리스트로 queue를 만들면 O(N)
#모듈을 사용하면 O(1)

###bfs
def hide_seek(n,k):
    
    queue = deque() 
    queue.append(n)

    while queue:
        
        location = queue.popleft()
        
        if location == k:
            return time[location]
        
        ###search
        for nx in [location-1,location+1,location*2]:
            ###위치가 범위에 있거나, 방문하지 않았을 경우
            if 0 <= nx < limit and time[nx]==0:
                ###초를 증가
                time[nx] = time[location] + 1
                queue.append(nx)
    

if __name__=='__main__':
    N, K = map(int,input().split())
    limit = 100001
    time = [0]*limit
    print(hide_seek(N,K))


