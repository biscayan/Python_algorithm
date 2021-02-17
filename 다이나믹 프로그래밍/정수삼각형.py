import sys

sys.stdin = open("input.txt", "r")

def int_triangle(dp_table):

    for i in range(1, n):
        for j in range(i+1):
            ### 첫번째 열은 대각선 오른쪽 위에서 내려옴
            if j == 0:
                dp_table[i][j] = dp_table[i][j] + dp_table[i-1][j]
            ### 마지막 열은 대각선 왼쪽 위에서 내려옴
            elif j == i:
                dp_table[i][j] = dp_table[i][j] + dp_table[i-1][j-1]
            ### 그 외에은 대각선 왼쪽 위, 오른쪽 위 모두에서 내려옴
            else:
                dp_table[i][j] = dp_table[i][j] + max(dp_table[i-1][j], dp_table[i-1][j-1])

    ### 마지막 행에서 가장 큰 값이 정답
    result = max(dp_table[n-1])

    return result


if __name__ == '__main__':

    n = int(sys.stdin.readline())

    array = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    print(int_triangle(array))