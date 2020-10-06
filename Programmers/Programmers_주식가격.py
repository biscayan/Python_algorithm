def solution(prices):

    answer=[0]*(len(prices)) #initialize the return array with zeros
    
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]: #compare i-th and j-th value
                answer[i]+=1 #save the return value in the array
            else:
                answer[i]+=1
                break # if the value decreases, stop the algorithm
        
    return answer

if __name__=='__main__':
    #test case1
    prices=[1,2,3,2,3]
    print(solution(prices))
    
