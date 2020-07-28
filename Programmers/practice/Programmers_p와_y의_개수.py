def solution(s):
    p=s.count('p')+s.count('P')
    y=s.count('y')+s.count('Y')
    if p==y:
        answer=True
    elif p!=y:
        answer=False
    else:
        answer=True
    return answer
