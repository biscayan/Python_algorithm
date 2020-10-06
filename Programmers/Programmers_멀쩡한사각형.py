import math

def solution(w,h):
    white_box=w+h-(math.gcd(w,h)) #최대공약수
    answer=w*h-white_box
    return answer


if __name__=='__main__':
    #test case
    W=8
    H=12
    print(solution(W,H))
