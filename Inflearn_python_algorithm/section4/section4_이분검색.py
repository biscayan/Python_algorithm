import sys

sys.stdin = open("input.txt","r")


N,M=map(int,input().split())
num_list=list(map(int,input().split()))
sorted_list=sorted(num_list)

print(sorted_list)

###방법1
#print(sorted_list.index(M)+1)

###방법2
l_idx = 0
r_idx = N-1

while l_idx<=r_idx:
    
    m_idx = (l_idx+r_idx)//2
    
    if sorted_list[m_idx]==M:
        print(m_idx+1)
        break
    
    ###왼쪽을 탐색
    elif sorted_list[m_idx]>M:
        r_idx = m_idx-1

    ###오른쪽을 탐색
    elif sorted_list[m_idx]<M:
        l_idx = m_idx+1

    
