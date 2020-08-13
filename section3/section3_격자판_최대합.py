import sys

sys.stdin=open('input.txt','r')

N=int(input())

lattice=[list(map(int,input().split())) for _ in range(N)]
#print(lattice)

num_list=[]

sum_ldi,sum_rdi=0,0

for i in range(N):

    #initialize the variables at every for loop
    sum_row,sum_col,=0,0

    for j in range(N):

        #sum of row
        sum_row+=lattice[i][j]
        
        #sum of column
        sum_col+=lattice[j][i]

        #sum of left diagonal
        if i==j:
            sum_ldi+=lattice[i][j]

        #sum of right diagonal
        if i+j==N-1:
            sum_rdi+=lattice[i][j]
    
    num_list.append(sum_row)
    num_list.append(sum_col)

num_list.append(sum_ldi)
num_list.append(sum_rdi)

print(max(num_list))