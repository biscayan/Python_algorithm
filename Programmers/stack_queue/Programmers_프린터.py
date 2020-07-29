def solution(priorities,location):

    answer=0
    
    while priorities: #while the array is not empty
        
        max_value=max(priorities)
        
        if priorities[0]==max_value: #find the max value of the array
            priorities.pop(0)
            
            answer+=1

            if location==0:
                return answer
            else: #next location
                location-=1
        else:
            wait=priorities.pop(0)
            priorities.append(wait)

            if location==0:
                location=len(priorities)-1
            else:
                location-=1

    return answer


if __name__=='__main__':
    #test case1
    priorities=[2,1,3,2]
    location=2
    print(solution(priorities,location))
    
    #test case2
    priorities=[1,1,9,1,1,1]
    location=0
    print(solution(priorities,location))


