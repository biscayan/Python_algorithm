import sys

sys.stdin = open("input.txt","r")

def Recruit(people_list):

    global N

    ###서류를 기준으로 내림차순 정렬
    sorted_people_list = sorted(people_list)
    #print(sorted_people_list)

    ###면접 순위가 가장 낮은 사람(숫자가 큼)을 기준으로 함
    lowest_rank = sorted_people_list[0][1]

    for i in range(1,N):

        ###면접 순위가 더 낮다면 탈락시킴
        if sorted_people_list[i][1] > lowest_rank:           
            N-=1
            
        ###그렇지 않다면 기준이 되는 사람을 바꿈
        else:
            lowest_rank = sorted_people_list[i][1]
    
    print(N)
    
if __name__ == '__main__':

    test_case = int(sys.stdin.readline())

    for _ in range(test_case):

        N = int(sys.stdin.readline())
        
        candidate = []

        for _ in range(N):
            paper, interview = map(int,sys.stdin.readline().split())
            candidate.append((paper,interview))
        
        Recruit(candidate)