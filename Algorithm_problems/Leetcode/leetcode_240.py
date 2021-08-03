# solution 1.
# runtime : 176 ms
# memory : 20.4 MB
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][-1] >= target:
                if matrix[i][j] == target:
                    return True
    return False

# solution 2.
# runtime : 152 ms
# memory : 20.7 MB
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n-1
    while row<=m-1 and col>=0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        elif matrix[row][col] == target:
            return True
        
    return False