def solution(n):
    rev_num = ''
    while n>0:
        n, mod = divmod(n,3)
        rev_num += str(mod)
    return int(rev_num,3)