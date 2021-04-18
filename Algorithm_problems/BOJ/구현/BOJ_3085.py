import sys

sys.stdin = open("input.txt", "r")


def check_row(n):

    global answer

    for i in range(n):        
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1
            
        answer = max(answer, cnt)


def check_col(n):

    global answer

    for i in range(n):        
        cnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1
            
        answer = max(answer, cnt)


def candy_game(n):

    global answer

    ### swap elements of row
    for i in range(n):
        for j in range(n-1):       
            if board[i][j] != board[i][j+1]:
                ### swap
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

                ### check rows and columns 
                check_row(n)
                check_col(n)

                ### reswap
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    ### swap elements of column
    for i in range(n):
        for j in range(n-1):    
            if board[j][i] != board[j+1][i]:
                ### swap
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

                ### check rows and columns 
                check_row(n)
                check_col(n)

                ### reswap
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

    print(answer)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    answer = 0

    candy_game(N)