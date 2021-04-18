def solution(heights):

    answer=[0]*len(heights)

    for i in range(len(heights)-1,-1,-1): #from the last index to the first index
        for j in range(i-1,-1,-1): 
            if heights[i]<heights[j]: #receive the signal at the lower tower
                answer[i]=j+1
                break
            
    return answer

if __name__=='__main__':
    #test case1
    heights=[6,9,5,7,4]
    print(solution(heights))

    #test case2
    heights=[3,9,9,3,5,7,2]
    print(solution(heights))

    #test case3
    heights=[1,5,3,6,7,6,5]
    print(solution(heights))
