import sys

sys.stdin = open("input.txt", "r")

def calc_date(e,s,m):

    cnt_e, cnt_s, cnt_m = 0, 0, 0
    answer = 0

    while True:

        cnt_e += 1
        cnt_s += 1
        cnt_m += 1

        answer += 1

        ### 범위를 넘어가면 1로 바꿈
        if cnt_e == 16:
            cnt_e = 1
        if cnt_s == 29:
            cnt_s = 1
        if cnt_m == 20:
            cnt_m = 1

        ### 원하는 값을 찾았다면 반복문 종료
        if cnt_e == e and cnt_s == s and cnt_m == m:
            break

    return answer


if __name__ == '__main__':

    E, S, M = map(int, sys.stdin.readline().split())
    print(calc_date(E,S,M))