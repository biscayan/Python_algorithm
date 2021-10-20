def count_divisor(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        div = count_divisor(num)
        if div%2 == 0:
            answer += num
        else:
            answer -= num
    return answer