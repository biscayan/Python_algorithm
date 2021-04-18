import sys

sys.stdin=open("input.txt","r")

N=int(input())
n_list=list(map(int,input().split()))

M=int(input())
m_list=list(map(int,input().split()))


###방법1
concat_list=sorted(n_list+m_list)
print(' '.join(map(str,concat_list)))

###방법2 (강의)
n=m=0
concat_list=[]

while n<N and m<M:
    if n_list[n]<m_list[m]:
        concat_list.append(n_list[n])
        n+=1
    else:
        concat_list.append(m_list[m])
        m+=1

if n==N:
    concat_list=concat_list+m_list[m:]
elif m==M:
    concat_list=concat_list+n_list[n:]

print(' '.join(map(str,concat_list)))


