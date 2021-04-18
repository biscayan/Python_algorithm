import sys

sys.stdin = open("input.txt","r")

def rope(array):

    ### 중량을 제일 큰 로프로 초기화
    w = array[0]
    count = 1

    for i in range(1, len(array)):

        count += 1
        cur_w = array[i] * count

        ### 현재의 중량이 기존의 중량보다 무거우면 값을 바꿈
        if cur_w > w:
            w = cur_w

    return w


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    rope_list = []

    for _ in range(N):
        r = int(sys.stdin.readline())
        rope_list.append(r)

    ### 로프를 내림차순으로 정렬
    rope_list = sorted(rope_list, reverse = True)

    print(rope(rope_list))