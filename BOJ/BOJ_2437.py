import sys

sys.stdin = open("input.txt","r")

def Scale(num_list):

    sorted_num_list = sorted(num_list)

    result = 0

    for num in sorted_num_list:
        ###지금까지 더한 값+1이 현재 들어오는 값보다 작게 되면 이것이 측정할 수 없는 무게가 됨
        if num > result+1:
            return result+1
        else:
            result += num

    return result+1

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    weights = list(map(int,sys.stdin.readline().split()))

    print(Scale(weights))