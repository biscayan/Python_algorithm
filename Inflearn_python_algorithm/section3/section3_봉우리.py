import sys

sys.stdin = open("input.txt", "r")

N = int(input())
map_info = [list(map(int,input().split())) for _ in range(N)]

def make_map(n,lattice):
    
    zero_line = [0]*(N+2)

    #add zero line at the top and the bottom
    lattice.insert(0,zero_line)
    lattice.append(zero_line)  

    #add zeros at the side
    for i in range(1,N+1,1):
        lattice[i].insert(0,0)
        lattice[i].append(0)

    return lattice

map_lattice = make_map(N,map_info)

top = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#방법1
for i in range(1,N+1):
    for j in range(1,N+1):
        #all -> 안의 조건이 모두 참일 때 참
        if all(map_lattice[i][j] > map_lattice[i+dx[k]][j+dy[k]] for k in range(4)):
            top+=1  

'''
#방법2
for i in range(1,N+1):
    for j in range(1,N+1):
        if map_lattice[i][j] > map_lattice[i-1][j] and map_lattice[i][j] > map_lattice[i][j-1] and map_lattice[i][j] > map_lattice[i+1][j] and map_lattice[i][j] > map_lattice[i][j+1]:
            top+=1
'''        
            
print(top)
