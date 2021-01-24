import sys

sys.stdin = open("input.txt","r")

def make_ricecake(array, start, end):

    result = 0

    while start <= end:

        num_sum = 0

        mid = (start + end) // 2

        for ricecake in array:
            if ricecake > mid:
                num_sum += (ricecake-mid)

        if num_sum >= M:

            ### 오른쪽 탐색, 절단기의 높이를 올림
            start = mid + 1

            ### 절단기의 최대높이를 찾아나감
            if mid > result:
                result = mid
        
        ### M만큼의 떡을 확보할 수 없음
        elif num_sum < M:
            ### 왼쪽 탐색, 절단기의 높이를 낮춤
            end = mid - 1

    return result


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())
    ricecakes = list(map(int, sys.stdin.readline().split()))

    max_height = make_ricecake(ricecakes, 0, max(ricecakes))
    print(max_height)