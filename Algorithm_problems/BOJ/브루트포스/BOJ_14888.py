import sys

sys.stdin = open("input.txt", "r")

### Brute-force
def calculation(lvl, num_sum):

    global plus, minus, mul, div, min_num, max_num

    if lvl == N:
        min_num = min(min_num, num_sum)
        max_num = max(max_num, num_sum)

    else:
        if plus > 0:
            plus -= 1
            calculation(lvl+1, num_sum+num_list[lvl])
            plus += 1
        
        if minus > 0:
            minus -= 1
            calculation(lvl+1, num_sum-num_list[lvl])
            minus += 1
        
        if mul > 0:
            mul -= 1
            calculation(lvl+1, num_sum*num_list[lvl])
            mul += 1
        
        if div > 0:
            div -= 1
            calculation(lvl+1, int(num_sum/num_list[lvl]))
            div += 1


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    
    num_list = list(map(int, sys.stdin.readline().split()))
    
    plus, minus, mul, div = map(int, sys.stdin.readline().split())

    ### 10억, -10억으로 초기화
    min_num, max_num = 1e9, -1e9

    calculation(1, num_list[0])

    print(max_num)
    print(min_num)