import sys
from collections import deque

sys.stdin = open('input.txt','r')
N, K = map(int,list(sys.stdin.readline().split()))

###range로 list를 바로 만들 수 있음
prince_list = list(range(1,N+1))
###list를 deque화시킴
prince_queue = deque(prince_list)

answer = 0

while prince_queue:
    for i in range(K):
        if i == K-1:
            prince_queue.popleft()
        else:
            popped_prince = prince_queue.popleft()
            prince_queue.append(popped_prince)
    ###마지막 남은 왕자
    if len(prince_queue) == 1:
        answer = prince_queue[0]

print(answer)