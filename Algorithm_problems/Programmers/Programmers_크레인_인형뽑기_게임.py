def solution(board, moves):

    answer = 0

    stack = []

    ###이중for문을 통해 column에 있는 인형들을 뽑음
    for col in moves:
        for row in range(len(board)):
            
            ###비어있는 칸(0)은 pass
            if board[row][col-1] != 0:
                stack.append(board[row][col-1])
                board[row][col-1] = 0
                break

        ###인형 터트리기
        if len(stack)>=2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer+=1

    ###인형 2개가 동시에 터지므로 *2를 해줘야함
    return answer*2            
        
if __name__=='__main__':
    
    ###test case
    
    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]

    moves = [1,5,3,5,1,2,1,4]
    
    print(solution(board, moves))
    
