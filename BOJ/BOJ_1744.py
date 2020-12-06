import sys
from collections import deque

sys.stdin = open("input.txt","r")

def Bind_num(num_list):

    ###내림차순으로 정렬
    sorted_num_list = sorted(num_list,reverse=True)

    ###시간복잡도 개선을 위해 리스트를 데크로 전환
    num_deque = deque(sorted_num_list)

    result = 0

    while num_deque:
        if len(num_deque) == 1:
            result += num_deque.popleft()

        else:
            ###1보다 클 때
            if num_deque[0]>1:

                ###다음 값이 1보다 크면 묶음
                if num_deque[1]>1:
                    result += (num_deque.popleft()*num_deque.popleft())

                ###다음값이 1이하이면 현재값만 더함
                elif num_deque[1]<=1:
                    result += num_deque.popleft()

            ###1이면 현재값만 더함
            elif num_deque[0]==1:
                result += num_deque.popleft()

            ###0일 때
            elif num_deque[0]==0:

                ###남은 수가 홀수개면 현재값만 더함
                if len(num_deque)%2==1:
                    result += num_deque.popleft()

                ###남은 수가 짝수개면 묶음
                else:
                    result += (num_deque.popleft()*num_deque.popleft())

            ###음수일 때
            elif num_deque[0]<0:

                ###남은 수가 홀수개면 현재값만 더함
                if len(num_deque)%2==1:
                    result += num_deque.popleft()

                ###남은 수가 짝수개면 묶음
                else:
                    result += (num_deque.popleft()*num_deque.popleft())

    print(result)

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    sequence = []

    for _ in range(N):
        num =int(sys.stdin.readline())
        sequence.append(num)
    
    Bind_num(sequence)