import sys

sys.stdin = open("input.txt", "r")

grid = [list(map(int,input().split())) for _ in range(7)]

answer = 0

for i in range(3):
    for j in range(7):
        
        ###row check
        row_check = grid[j][i:i+5]
        if row_check==row_check[::-1]:
            answer+=1

        ###column check
        for k in range(2):
            if grid[i+k][j]!=grid[i+5-k-1][j]:
                break
        else:
            answer+=1

            
print(answer)
