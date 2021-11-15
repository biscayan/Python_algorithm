def solution(s):
    step, total_zero = 0, 0
    while s != '1':
        s_len = len(s)
        zero_cnt = s.count('0')
        total_zero += zero_cnt
        s = bin(int(s_len - zero_cnt))[2:]
        step += 1
    return [step, total_zero]