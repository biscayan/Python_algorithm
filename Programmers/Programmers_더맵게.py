import heapq

def solution(sco_list,k):
    
    answer = 0

    ###힙으로 변환
    heapq.heapify(sco_list)
    
    while len(sco_list) >= 2:
        
        ###가장 작은 요소가 k를 넘으면 중단
        if sco_list[0] >= k:
            return answer

        else:
            scovile1 = heapq.heappop(sco_list)
            scovile2 = heapq.heappop(sco_list)

            new_scovile = scovile1 + (scovile2*2)
            heapq.heappush(sco_list,new_scovile)

            answer+=1

    ###모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
    if sco_list[0] < k:
        return -1
    else:
        return answer

if __name__=='__main__':
    ###test case
    scovile = [1,2,3,9,10,12]
    K = 7

    print(solution(scovile,K))