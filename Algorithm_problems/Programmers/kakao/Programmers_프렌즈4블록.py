def solution(m, n, board):
    answer = 0
    new_board = []
    for string in board:
        new_board.append(list(string))

    while True:
        # 순서를 정할 수 있다면 set이 좋을텐데..
        remove = []
        flag = False
        for i in range(m-1):
            for j in range(n-1):
                if type(new_board[i][j]) == str and new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1]:
                    if (i,j) not in remove:
                        remove.append((i,j))
                    if (i,j+1) not in remove:
                        remove.append((i,j+1))
                    if (i+1,j) not in remove:
                        remove.append((i+1,j))
                    if (i+1,j+1) not in remove:
                        remove.append((i+1,j+1))
                    flag = True

        if not flag:
            break
        
        for x, y in remove:
            while x > 0:
                new_board[x][y] = new_board[x-1][y]
                new_board[x-1][y] = 0
                x -= 1
            answer += 1

    return answer