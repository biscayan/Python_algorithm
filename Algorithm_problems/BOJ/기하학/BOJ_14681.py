import sys

sys.stdin = open("input.txt", "r")

def Four_areas(x,y):

    if x>0 and y>0:
        print(1)
    elif x<0 and y>0:
        print(2)
    elif x<0 and y<0:
        print(3)
    elif x>0 and y<0:
        print(4)


if __name__ == '__main__':

    X, Y = int(sys.stdin.readline()), int(sys.stdin.readline())

    Four_areas(X, Y)