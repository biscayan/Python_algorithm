from collections import deque

def topological_sort():

    queue = deque()

    result = []

    ### 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            
            indegree[i] -= 1

            ### 진입차수가 0인 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    ### 정렬 결과를 출력
    for node in result:
        print(node, end=' ')
        

if __name__ == '__main__':

    v, e = map(int, input().split())

    indegree = [0] * (v+1)

    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        ### a에서 b로 이동
        graph[a].append(b)
        ### b로 가는 진입차수를 1 증가
        indegree[b] += 1

    topological_sort()