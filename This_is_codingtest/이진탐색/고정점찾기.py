import sys

sys.stdin = open("input.txt", "r")

def find_fixedpoint(array,start,end):

    while start <= end:
        
        mid = (start+end) // 2

        if mid == array[mid]:
            return mid
        
        elif array[mid] > mid:
            end = mid-1

        elif array[mid] < mid:
            start = mid+1

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    num_list = list(map(int,sys.stdin.readline().split()))

    fixed_point = find_fixedpoint(num_list,0,N-1)

    if fixed_point == None:
        print(-1)
    else:
        print(fixed_point)