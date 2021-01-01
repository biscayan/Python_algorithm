import sys
from collections import deque

sys.stdin = open("input.txt","r")

def printer_queue(n, m, num_list):
    
    result = 0

    queue = deque([])
    
    for i in range(n):
        queue.append((num_list[i],i))
    
    while queue:
        
        ### 리스트에서 최고 우선순위
        first_prior = max(queue)[0]
        
        num_prior, num_seq = queue.popleft()
        
        ### 최고 우선순위와 아이템의 우선순위가 같으면
        if first_prior == num_prior:
            
            result += 1
            
            ### 알아내고자 하는 아이템을 만나면 return
            if m == num_seq:
                return result

        else:
            queue.append((num_prior,num_seq))
                

if __name__ == '__main__':

    test_case = int(sys.stdin.readline())

    for _ in range(test_case):

        N, M = map(int, sys.stdin.readline().split())

        nums = list(map(int, sys.stdin.readline().split()))
        
        print(printer_queue(N, M, nums))