def solution(progresses,speeds):

    answer=[]
    
    while progresses: #while the array is not empty
        for i in range(len(progresses)):
            progresses[i]+=speeds[i] #repeat the work
            
        distribution=0
        
        while progresses and progresses[0]>=100: #check the threshold=100
            progresses.pop(0)
            speeds.pop(0)
            distribution+=1

        if distribution!=0:
            answer.append(distribution)
            
    return answer

if __name__=='__main__':
    #test case1
    progresses=[93,30,55]
    speeds=[1,30,5]
    print(solution(progresses,speeds))
    
