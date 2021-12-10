def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)
    cnt = 0
    for l in new_lost:
        if l-1 in new_reserve:
            new_reserve.remove(l-1)
            cnt += 1
        elif l+1 in new_reserve:
            new_reserve.remove(l+1)
            cnt += 1
    return answer+cnt