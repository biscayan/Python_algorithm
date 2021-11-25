import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")

def num_baseball(num_list):
    answer = 0
    per_list = list(permutations([1,2,3,4,5,6,7,8,9],3))
    for per in per_list:
        flag = True
        for i in range(N):
            strike, ball = 0, 0
            for j in range(3):
                if num_list[i][0][j] == str(per[j]):
                    strike += 1
                elif num_list[i][0][j] != str(per[j]) and str(per[j]) in num_list[i][0]:
                    ball += 1
            if num_list[i][1] != strike or num_list[i][2] != ball:
                flag = False
                break
        if flag:
            answer += 1
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    num_list = []
    for _ in range(N):
        num, s, b = sys.stdin.readline().split()
        num_list.append((num,int(s),int(b)))
    print(num_baseball(num_list))