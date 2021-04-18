import sys
#sys.stdin=open("input.txt","rt")

N=input()
d_list=list(map(int,input().split()))

def digit_sum(x):
    d_sum=0
    while x>0:
        d_sum+=x%10
        x=x//10
    return d_sum

max_value=0

for x in d_list:
    max_cand=digit_sum(x)
    if max_cand>max_value:
        max_value=max_cand
        res=x

print(res)
