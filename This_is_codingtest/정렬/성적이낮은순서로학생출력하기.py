import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def print_student(array):

    sorted_array = sorted(array, key = lambda score:score[1])
    
    for items in sorted_array:
        print(items[0], end=' ')

if  __name__ == '__main__':

    N = int(sys.stdin.readline())
    
    array = []

    for _ in range(N):
        student, score = sys.stdin.readline().split()
        array.append((student,int(score)))
    
    print_student(array)