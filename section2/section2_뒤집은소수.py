import sys
sys.stdin=open("input.txt","rt")

N=int(input())
num_list=list(map(int,input().split()))

def reverse(x):
    res=0
    while x>0:
        num=x%10
        res=res*10+num
        x=x//10
    return res

def isPrime(x):
    if x==1: #1을 소수로 처리해서는 안됨
        return False
    for i in range(2,x//2+1): #숫자의 절반까지만 확인해도됨
        if x%i==0:
            return False
    else:
        return True

for x in num_list:
    reversed_num=reverse(x)
    if isPrime(reversed_num):
        print(reversed_num,end=' ')
    


