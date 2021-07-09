import sys

sys.stdin = open("input.txt", "r")

def two_liquid(liquid_list):

    # The largest possible value
    value = 2e9

    l_idx, r_idx = 0, N-1

    while l_idx < r_idx:

        mixed = liquid_list[l_idx] + liquid_list[r_idx]

        if abs(mixed) < value:
            result_list = [liquid_list[l_idx], liquid_list[r_idx]]
            value = abs(mixed)

        if mixed == 0:
            break
        elif mixed < 0 : 
            l_idx += 1
        else:
            r_idx -= 1

    print(result_list[0], result_list[1])

    
if __name__ == '__main__':

    N = int(sys.stdin.readline())
    liquid_list = list(map(int,sys.stdin.readline().split()))

    liquid_list.sort()

    two_liquid(liquid_list)