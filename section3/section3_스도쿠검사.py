import sys

sys.stdin = open("input.txt","r")

def sudoku(puzzle):

    for i in range(9):
        
        row_check = [0]*10
        col_check = [0]*10
        
        for j in range(9):
            
            row_check[puzzle[i][j]] = 1
            col_check[puzzle[j][i]] = 1

        if sum(row_check)!=9 or sum(col_check)!=9 :
            return False
        
    ###search groups
    for i in range(3):
        for j in range(3):
            
            group_check = [0]*10

            ###search elements
            for k in range(3):
                for l in range(3):
                    group_check[puzzle[i*3+k][j*3+l]] = 1

            if sum(group_check)!=9:
                return False
            
    ###조건을 모두 통과        
    return True   
            

if __name__=="__main__":
    
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    ###참이면 YES, 거짓이면 NO
    if sudoku(puzzle):
        print("YES")
    else:
        print("NO")

    

