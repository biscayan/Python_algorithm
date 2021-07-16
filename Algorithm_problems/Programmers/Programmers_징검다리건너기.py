def solution(stones, k):

    answer = 0
    left, right = 1, max(stones)
    
    while left <= right:

        # 0이 된 stone의 개수
        count = 0
        # 건널 수 있는 니니즈의 수
        mid = (left+right) // 2

        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break

        if count < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid

    return answer