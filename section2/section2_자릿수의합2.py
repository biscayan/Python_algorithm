import sys
#sys.stdin=open("input.txt","rt")

N=input()
d_list=list(map(int,input().split()))

def digit_sum(x):
    d_sum=0
    for i in str(x):
        d_sum+=int(i)
    return d_sum

max_value=0

for x in d_list:
    max_cand=digit_sum(x)
    if max_cand>max_value:
        max_value=max_cand
        res=x

print(res)
