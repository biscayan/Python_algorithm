import sys

sys.stdin = open("input.txt", "r")

def div_conq(x,y,size):

    global count

    if x==r and y==c:
        print(count)
        return 

    if size == 1:
        count += 1
        return

    if not (x<=r<x+size and y<=c<y+size):
        count += size*size
        return

    div_conq(x,y,size//2) # 1사분면
    div_conq(x,y+size//2,size//2) # 2사분면
    div_conq(x+size//2,y,size//2) # 3사분면
    div_conq(x+size//2,y+size//2,size//2) # 4사분면


if __name__ == '__main__':

    N, r, c = map(int, sys.stdin.readline().split())
    count = 0
    
    div_conq(0,0,2**N)