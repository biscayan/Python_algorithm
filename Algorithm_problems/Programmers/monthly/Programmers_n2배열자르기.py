def solution(n, left, right):
    array = []
    for i in range(left,right+1):
        q, r = divmod(i,n) 
        array.append(max(r,q)+1)
    return array