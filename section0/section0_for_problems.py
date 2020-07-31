N=10

'''
#1. 1부터 N까지 홀수출력하기
for i in range(1,N+1):
    if i%2==1:
        print(i)
'''

'''
#2. 1무터 N까지의 합 구하기
s=0
for i in range(1,N+1):
    s=s+i
print(s)
'''

#3. N의 약수출력하기
for i in range(1,N+1):
    if N%i==0:
        print(i)

