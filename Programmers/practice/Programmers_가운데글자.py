def solution(s):
    len(s)>=1 and len(s)<=100
    if len(s)%2==1:
        n=len(s)//2
        return s[n]
    elif len(s)%2==0:
        n=len(s)//2
        return s[n-1]+s[n]

print(solution("abcde"))
print(solution("qwer"))
