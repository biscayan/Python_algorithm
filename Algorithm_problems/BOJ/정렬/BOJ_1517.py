import sys

sys.stdin = open("input.txt", "r")

def merge(l_arr, r_arr):

    global answer

    l_idx, r_idx = 0, 0
    tmp_arr = []
    
    while l_idx < len(l_arr) and r_idx < len(r_arr):
        if l_arr[l_idx] > r_arr[r_idx]:
            tmp_arr.append(r_arr[r_idx])
            r_idx += 1
            answer += len(l_arr) - l_idx
        else:
            tmp_arr.append(l_arr[l_idx])
            l_idx += 1

    if l_idx == len(l_arr):
        tmp_arr.extend(r_arr[r_idx:])
    else:
        tmp_arr.extend(l_arr[l_idx:])

    return tmp_arr

def merge_sort(arr):

    # can't divide anymore
    if len(arr) <= 1:
        return arr

    left, right = 0, len(arr)-1
    mid = (left+right) // 2

    merged_arr = merge(merge_sort(arr[left:mid+1]), merge_sort(arr[mid+1:]))

    return merged_arr

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    answer = 0
    merge_sort(array)
    print(answer)