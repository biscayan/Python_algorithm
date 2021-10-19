def solution(numbers):
    not_in_numbers = [i for i in range(10)]
    for num in numbers:
        not_in_numbers[num] = 0
    return sum(not_in_numbers)