import sys

sys.stdin = open("input.txt", "r")

def Alibaba(n):

    dp_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0:
                ### 시작지점
                if j == 0:
                    dp_table[i][j] = board[i][j]
                ### 첫번째 행은 오른쪽으로만 이동 가능
                else:
                    dp_table[i][j] = dp_table[i][j-1] + board[i][j]
            else:
                ### 첫번째 열은 밑으로만 이동 가능
                if j == 0:
                    dp_table[i][j] = dp_table[i-1][j] + board[i][j]
                ### 첫번째 행/첫번째 열이 아닐 경우, 위에서 오는 것과 왼쪽에서 오는 것 중에서 최소값을 저장
                else:
                    dp_table[i][j] = min(dp_table[i][j-1] + board[i][j], dp_table[i-1][j] + board[i][j])

    ### 도착지점
    result = dp_table[n-1][n-1]

    print(result)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    Alibaba(N)